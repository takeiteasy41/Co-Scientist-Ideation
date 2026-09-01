# Known Pitfalls

## Discovery scope is part of the result

A Skill found in one project's `.agents/skills` is project-scoped evidence. It does not prove that an
unrelated project can discover the same Skill. For cross-project use, install the complete package in a
supported user-level Skill root and run one explicit discovery smoke from an unrelated working
directory. Keep same-name copies out of competing roots during the smoke so the resolved source is
observable.

`allow_implicit_invocation: false` is intentional. Discovery and activation are separate: the package
can be installed and explicitly invoked while ordinary tasks remain unaffected.

## Non-Git directories cannot create valid Git worktrees

Before creating a Codex task, check whether the project has a valid Git `HEAD`. A directory that merely
contains source files is not necessarily a usable Git repository. Use a local/direct environment for a
non-Git project; otherwise worktree setup can fail with an invalid-reference error before the task sees
the prompt.

## Network availability is not evidence admission

The Skill uses a per-run offline/Web boundary. Globally disabling Web reduces useful verification;
globally trusting Web results weakens evidence quality. Search snippets and model memory are discovery
leads. A claim becomes admissible only after an allowed source is opened and the relevant passage,
scope, relation and limitation are checked.

Unpublished details can leak through search queries even when no file is uploaded. Abstract queries by
default and decide which details may leave the workspace before retrieval begins.

## Domain examples can become accidental hard-coding

Examples are useful only when they instantiate a general check. Keep the underlying contract
domain-neutral:

- data work: provenance, split unit, leakage, duplicates, baselines and uncertainty;
- physical or biological work: entities, units, boundary conditions, controls and independent units;
- formal or systems work: interfaces, assumptions, bottlenecks, matched isolation and local
  falsifiers.

Do not promote a field-specific dataset, mechanism, metric, model family or intervention into a
universal default. A new example should be removable without changing the workflow's meaning.

## Opened-source evidence and package prose can diverge

A rich hypothesis package may still contain one unsupported exact number or source-specific statement.
This occurred in the retained evaluation and was treated as a substantive `SOURCE_MISUSE`, not a
formatting defect. Audit exact numbers, dates, rankings and named-source comparisons separately from
the overall quality of the idea.

## “No finalist” can be the correct endpoint

The workflow is designed to stop when evidence, authorization, privacy, safety, expertise or budget is
insufficient. Filling a quota after a failed producer or repairing a decisive gap from memory converts
an honest scientific stop into unsupported confidence. Preserve the no-finalist package and state the
cheapest next evidence needed.

## Independence can be weaker than it looks

Temporary subagents may share a model family or inherited context. Spawn peers before either peer's
answer is returned, remove author/arm labels from review envelopes, and disclose unavailable
independence. A fresh reviewer is a workflow control, not proof of human or statistical independence.

Parent rollout/session traces are ephemeral implementation evidence. Capture only the minimal relevant
trace when diagnosing a defect; do not expose private prompts, chain-of-thought or unrelated workspace
content in public artifacts.

## Windows paths and sandbox boundaries need exact handling

On Windows, quote paths containing spaces, resolve the exact target, verify direct-child containment,
and reject reparse points before moves or deletion. A more specific read-only boundary can override a
broader workspace-write permission. Use a narrowly scoped elevated operation only when the exact
deployment target requires it; never broaden that approval into a general shell rule.

For replacement or cleanup, prefer same-volume literal moves, an exact ledger and a closed allowlist.
Do not overwrite an occupied recovery target. Deletion begins only after the promoted tree, rollback
tree and receipts have been verified.

## Hash receipts can invalidate themselves

A manifest inside a tree cannot contain the final hash of that same tree unless an exact self-exclusion
rule is defined. Keep package-tree receipts outside the package, or explicitly exclude the receipt and
its sidecar. Moving a frozen evaluation tree can also break relative paths even when leaf bytes are
unchanged; preserve the original relative location when manifests refer to siblings or project-root
paths.

## Evaluation votes are nested

Reviewer choices are nested within pairs and tasks. Treating every reviewer vote as an independent
scientific replicate creates pseudoreplication. Report the frozen task-equalized descriptive endpoint,
the adverse critical-failure gate and fixed-task limitations together.

## Paper custody is not publication permission

A local corpus receipt proves byte custody, not copyright, privacy or redistribution rights. Keep the
paper corpus and raw pair artifacts ignored. Before public release, audit source licenses, downloaded
content, private identifiers, task mappings and any third-party terms separately.
