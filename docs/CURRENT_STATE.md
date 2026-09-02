# Current State

Date: `2026-09-02`  
Release: `co-scientist-ideation 1.9-rc1`  
Status: validated public release candidate  
Repository license: `Apache-2.0`

This document describes portable release facts. Per-machine installation and discovery results belong
in Git-ignored local receipts rather than public source files.

## Package custody

| Object | Files | Bytes | Canonical tree SHA-256 |
|---|---:|---:|---|
| Public Skill package | 13 | 101,602 | `b20e9479e53346938eed7299d8b4e5756df574cea0045be98e5e1ed291ee4899` |
| Validated payload excluding Manifest | 12 | 99,625 | `2c3bfec716fa41a927aedb7cc771f2cc056c89318458237e7d647763f0aa4649` |

The 12-file payload is byte-identical to the validated internal `1.9-rc1` payload. The public
`RELEASE_MANIFEST.yaml` is a portable receipt that omits machine paths, task/session identifiers,
usage totals, and private finalization history. Because a manifest cannot hash a tree containing
itself, the complete package receipt is stored outside the package and repeated here.

Canonical tree algorithm: ordinal-sorted forward-slash relative paths; one UTF-8 LF record per leaf as
`path<TAB>bytes<TAB>sha256<LF>`; SHA-256 over the concatenated record bytes.

## Behavioral invariants

- explicit invocation: `$co-scientist-ideation`;
- `policy.allow_implicit_invocation: false`;
- bounded six-block ideation ending in a human decision;
- normally 2–4 initial candidates and at most 3 concurrent temporary subagents;
- independent Review is mandatory for every promoted candidate;
- Web retrieval is run-scoped, permission-aware, and source-grounded rather than globally disabled;
- domain examples select relevant checks but do not supply domain-specific answers;
- code, training, experiments, data collection, writing, and external action require separate
  authorization.

## Validation baseline

| Check | Frozen result |
|---|---|
| Behavior and regression tests | `PASS_16_OF_16` |
| Structural validator | `PASS_13_FILES_ZERO_ERRORS_WARNINGS` |
| Official quick validator | `PASS` |
| Bounded real forward behavior | `PASS_ACCEPTED_NO_FINALIST` |
| Public privacy scan | `PASS` |

Commands from the repository root:

```powershell
python -m unittest discover -s .\co-scientist-ideation\tests -p test_scripts.py -q
python .\co-scientist-ideation\scripts\validate_skill.py
python -X utf8 "<path-to-skill-creator>\scripts\quick_validate.py" .\co-scientist-ideation
```

The forward check used one Web-authorized, non-computational biology ideation task. The workflow
opened authoritative sources, applied claim-use admission, obtained independent review, and returned
no finalist because the evidence did not justify promotion. This is a valid stopping outcome.

## Installation locations

The official portable user location documented by OpenAI is
`$HOME/.agents/skills/co-scientist-ideation`. A project may use
`<project>/.agents/skills/co-scientist-ideation`. The local host used for this release also discovers
`~/.codex/skills/co-scientist-ideation`; that path is host-specific. Copy the complete 13-file package
and verify it before invoking `$co-scientist-ideation` from an unrelated project.

## Retained endpoint-recomputation closure

The local ignored closure remains at `evaluation/comparative-efficacy/` so its project-relative and
sibling references retain their meaning.

| Tree | Files | Bytes | Canonical tree SHA-256 |
|---|---:|---:|---|
| `evaluation-method-v1` | 5 | 43,463 | `e59b0e34758c301c2228a51f94b338704ef088ab01cd402ed3ff9f02a6996bf3` |
| `v4-ai-followup-1.0` | 78 | 42,644,224 | `86e38dcefe76aad292772922c637925177326f6d4a71f09900adde5ee536e4ea` |
| `v4-ai-followup-1.1` | 8 | 52,772 | `d22a6b229fe4eeef5e27c75749f32fedb75dfcfaaac13f388943ea1bc5e58523` |
| `v4-ai-followup-1.2` | 8 | 45,514 | `b58910d74d00a84cde1fca4ce638b0a3785991dc8834cefa37745cab606729b8` |
| `v4-ai-followup-1.3` | 284 | 1,474,571 | `0d328654b34448750dda2255f70e55f38a8414888a50c30ad5fc4439f1629ef7` |
| `v4-ai-followup-1.4` | 48 | 135,864 | `8f578b1ac23d8b17489737e40e0639602cd877e4a76e4df53c604e3340d65e42` |

Combined: `431 files / 44,396,408 bytes`. The included paper corpus is `36 files /
42,400,715 bytes / 44dc80911fc16383d573a4c5926f5f644ccb75ce02d040127628744107a59880`.
Both the closure and private finalization receipts are Git-ignored.

This closure supports deterministic recomputation of the final descriptive endpoint and validation of
the retained records. It does not contain every historical task-selection, disjointness, host snapshot,
or model-execution dependency needed to rerun the full study or re-audit all upstream provenance.

## Known limits

- Local validation establishes package behavior under the tested host and tasks, not universal
  scientific quality.
- The comparative endpoint is AI-only, exploratory, based on four fixed tasks, and includes one
  Co-Scientist source-misuse failure.
- No human preference, confirmatory efficacy, scientific truth, or deployment ROI claim is licensed.
- The ignored paper corpus needs a separate source-license and privacy audit before publication.
- Repository-owned public contents are licensed under `Apache-2.0`; linked third-party materials and
  the ignored paper corpus remain outside that grant.

## Next legitimate maintenance action

For ordinary use, install the unchanged package and invoke it explicitly. If a reproducible Skill
defect appears, classify the failure first, preserve the minimal evidence privately, and write an
audited file-level change order for a new sibling version. See
[`MAINTENANCE_RUNBOOK.md`](MAINTENANCE_RUNBOOK.md).
