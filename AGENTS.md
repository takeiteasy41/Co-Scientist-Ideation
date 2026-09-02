# Repository Instructions

This repository maintains one public release candidate, `co-scientist-ideation/`, plus compact public
documentation and a Git-ignored local endpoint-recomputation closure.

## Authoritative state

- Release: `1.9-rc1`
- Public package: `13 files / 101,602 bytes`
- Public package canonical tree SHA-256:
  `b20e9479e53346938eed7299d8b4e5756df574cea0045be98e5e1ed291ee4899`
- Validated payload excluding `RELEASE_MANIFEST.yaml`: `12 files / 99,625 bytes`
- Payload canonical tree SHA-256:
  `2c3bfec716fa41a927aedb7cc771f2cc056c89318458237e7d647763f0aa4649`
- Invocation invariant: `policy.allow_implicit_invocation: false`
- Explicit name: `$co-scientist-ideation`

The canonical tree algorithm is ordinal-sorted forward-slash relative paths, one UTF-8 LF record per
leaf as `path<TAB>bytes<TAB>sha256<LF>`, followed by SHA-256 of those canonical bytes.

## Repository boundaries

- `co-scientist-ideation/` is the installable package and the only current Skill source.
- `docs/` describes current state, durable history, known pitfalls, and maintenance.
- `evaluation/README.md` and `evaluation/EVALUATION_SUMMARY.yaml` are public summaries.
- `evaluation/comparative-efficacy/` is a local, Git-ignored endpoint-recomputation closure. Treat it as
  read-only. It is not a complete model-experiment rerun package.
- `internal/` contains Git-ignored custody, audit, deployment, and cleanup receipts.

The repository owner's original public contents are licensed under Apache License 2.0. Linked
third-party sources and ignored evaluation papers remain under their own terms and are not relicensed.
Do not publish ignored evaluation papers or internal receipts without a separate source-license,
privacy, and provenance audit.

## Change discipline

1. Read `docs/CURRENT_STATE.md`, `docs/KNOWN_PITFALLS.md`, and
   `docs/MAINTENANCE_RUNBOOK.md` before changing the Skill.
2. Never patch a frozen release in place. Copy it to a clearly named sibling version and preserve the
   parent receipt.
3. Define a file-level change order with exact update/add/delete boundaries and a SHA-256 sidecar.
4. Obtain a fresh `fork_turns=none`, read-only adversarial audit whose first line is `PASS` before
   implementation or deployment.
5. Preserve the explicit-only policy, human-selection boundary, evidence admission gate, independent
   review, and separate execution authorization unless a new audited release decision changes them.
6. Run the smallest complete verification: behavior tests, structural validator, official quick
   validator, privacy scan, then a bounded real usage check when behavior changed.
7. A behavioral defect creates a new narrow sibling-version change order. Preserve the prompt, input,
   final output, and relevant trace in ignored custody; do not rewrite the released package.

Network retrieval is run-scoped. It may be used when authorized and decision-relevant, with opened
primary or authoritative sources and privacy-safe queries. Do not encode one scientific domain's
examples as universal defaults.

Historical efficacy work is frozen. Recomputing the retained endpoint is allowed for integrity checks;
new model requests, selective reruns, human-panel claims, publication, license changes, or a new
evaluation design require separate owner authorization.

## Verification

From the repository root:

```powershell
python -m unittest discover -s .\co-scientist-ideation\tests -p test_scripts.py -q
python .\co-scientist-ideation\scripts\validate_skill.py
python -X utf8 "<path-to-skill-creator>\scripts\quick_validate.py" .\co-scientist-ideation
python .\evaluation\comparative-efficacy\evaluation-method-v1\test_evaluation_method.py -q
```

Stop when the requested change and proportionate checks pass. Do not add a Manager, queue, database,
persistent memory, compatibility layer, runner, or evaluation platform unless a concrete authorized
requirement makes it necessary.
