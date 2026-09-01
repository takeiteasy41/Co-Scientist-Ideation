# Maintenance Runbook

Use this runbook for a narrow future change to `co-scientist-ideation`. It is a release procedure, not
an automated runner or a persistent research platform.

## 1. Establish custody

1. Read `CURRENT_STATE.md`, `KNOWN_PITFALLS.md`, the current `RELEASE_MANIFEST.yaml`, and the files that
   own the requested behavior.
2. Recompute the current package and payload receipts from disk. Treat bytes and tests as authority.
3. Classify the request: documentation-only, packaging, trigger/policy, scientific workflow, evidence
   contract, retrieval, or observed defect.
4. Confirm scope, installation target, network boundary, publication boundary and destructive actions.

Do not infer a Skill defect from one disappointing scientific answer. Separate:

- Skill defect: the frozen contract was violated on a valid task;
- task/prompt defect: the goal or evidence envelope was insufficient;
- evidence insufficiency: the correct outcome is uncertainty or no finalist;
- capacity/transport failure: the requested role or canonical output was unavailable;
- evaluation error: the judge, aggregation or custody was wrong.

## 2. Create a sibling version

Copy the current release to a new versioned sibling. Keep the parent byte-identical and record:

- parent full-tree and payload receipts;
- exact updated, added and deleted leaves;
- behavior that must remain unchanged;
- rollback source;
- explicit-only and human-control invariants.

Prefer the smallest file set that owns the observed seam. Examples belong in tests or references only
when they clarify a general contract; they must not turn one domain into the default.

## 3. Freeze a file-level change order

Before implementation, write one change order and SHA-256 sidecar containing:

- positive outcome and non-goals;
- exact file operations;
- acceptance commands and expected observations;
- source, deployment and evaluation protection boundaries;
- failure classification and rollback;
- whether Web retrieval is permitted for forward validation;
- claim limits for any scientific or comparative result.

Send it to a fresh `fork_turns=none`, read-only adversarial auditor. The first line must be `PASS` or
`FAIL`. On `FAIL`, replace or remove only the material blocker in the same order, update its sidecar,
and return it to the same auditor. Implementation starts only after `PASS`.

## 4. Implement and verify locally

Apply the audited leaf operations to the sibling, then run from the sibling root:

```powershell
python -m unittest discover -s .\tests -p test_scripts.py -q
python .\scripts\validate_skill.py
python -X utf8 "<path-to-skill-creator>\scripts\quick_validate.py" .
```

Also verify:

- exact payload/full-tree receipts and per-leaf diff;
- `agents/openai.yaml` keeps `allow_implicit_invocation: false` unless a separately audited decision
  explicitly changes it;
- trigger positives require explicit Co-Scientist-style scientific ideation;
- negative cases leave before retrieval, delegation or writes;
- public files contain no machine paths, usernames, private identifiers, secrets or raw traces;
- network behavior is run-scoped and source admission remains mandatory.

## 5. Run bounded forward validation when behavior changed

Choose the smallest real task that can expose the changed seam and still matters to a human decision.
Freeze the prompt, input/evidence envelope, model/runtime settings, network permission, task environment,
request ceiling and acceptance observations before launch.

For a non-Git project use local/direct execution. Do not create a worktree. Use one launch unless the
audited order explicitly authorizes a replacement. Preserve the original prompt, final output and
relevant trace privately if a defect appears.

A pass means the changed contract was observable, including a correct stop or no-finalist result. It
does not establish generic efficacy or scientific truth.

## 6. Freeze the public artifact

Create a clean public staging tree containing only the installable package, public docs and aggregate
evaluation summary. Keep corpora and internal receipts in ignored paths. Recompute:

- package and payload receipts;
- Git-visible public tree manifest;
- link and privacy scans;
- tests and validators from staging.

Use a second, different fresh read-only auditor for the actual staged artifact. A Gate B `PASS` freezes
all Git-visible bytes. A public correction after PASS requires a new deterministic check and Gate B
audit; machine-specific receipts remain ignored and may be written only in the named post-Gate-B
phases.

## 7. Promote to an installation target

Resolve the supported user or project Skill root for the current host. Ensure no competing same-name
Skill can mask the candidate. Promote the complete package with a same-volume replacement when
possible, retain the previous target until validation finishes, and run:

- behavior tests;
- structural and official validators;
- policy/privacy checks;
- one explicit `$co-scientist-ideation` discovery smoke from an unrelated working directory.

The smoke prompt asks the runtime to report the observed release, implicit policy and resolved Skill
path without supplying the expected values. One launch and zero retry keeps the observation
interpretable. On failure, restore only the exact previous target and stop.

## 8. Clean historical material only through a closed transaction

Create an ordinal top-level ledger and verify staging, quarantine and failed-finalization names are
absent, ordinary direct children and free of reparse points. Move originals to exact quarantine, move
the frozen final entries to root, remove only an exact empty staging directory, and check a closed
allowlist.

Before recursive deletion, verify package equality, evaluation receipts, public links, privacy,
personal discovery and transaction journal custody. Move the final journal outside quarantine and
verify its hash. Once quarantine deletion begins, the historical tree is no longer a rollback source;
an interruption may resume only against its exact manifest.

## 9. Stop and hand off

Record the final package/payload/public-tree/project receipts, audit response hashes, validation
commands, installed target class, smoke outcome, retained evaluation receipt and removed categories.
Then stop. Further optimization, new evaluation requests, license selection, Git publication or a new
scientific experiment is a separate decision.
