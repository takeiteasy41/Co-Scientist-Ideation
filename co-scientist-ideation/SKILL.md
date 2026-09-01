---
name: co-scientist-ideation
description: >-
  Guides a parent Codex through a bounded, idea-first six-block research-ideation process with evidence mapping,
  mechanistically distinct hypotheses, independent review, conditional comparison, objection-driven evolution,
  fresh review, and human selection. Use only when the user explicitly invokes $co-scientist-ideation with a
  scientific ideation goal, asks to run or imitate Co-Scientist, says 多智能体科研构思 or 科研搭档想点子, or asks
  multiple scientific roles to propose and screen research hypotheses. Merely mentioning Co-Scientist or subagents
  does not trigger it. Do not trigger for software development, debugging, code review, parallel exploration,
  literature summaries, experiment execution, or paper writing.
---
# Co-Scientist Ideation

Release: `1.9-rc1`; retrieval is run-scoped and multi-component checks are domain-neutral.

## Purpose

Help a scientist find an important evidence-grounded problem, produce a small set of coherent and
falsifiable ideas, expose their killer objections, materially repair a promising idea when justified,
and make the remaining decision human-owned. This is a Codex Skill, not a research platform.

## Trigger gate

Run this gate before retrieval, delegation, or file creation.

- Pass only for explicit Co-Scientist-style scientific ideation with role-separated generation and
  screening.
- The words `Co-Scientist`, `agent`, or `subagent` alone do not pass.
- Route ordinary brainstorming, observation-to-hypothesis work, project framing, literature review,
  experiment design, coding, and paper writing to their normal owners.
- If the gate fails, leave this Skill silently. See [activation rules](references/localization.md).

## Operating contract

The parent Codex is a bounded Supervisor inside the current task. It owns authorization, admission,
synthesis, and human interaction. Temporary subagents are cognitive perspectives, not resident Agents
or human experts. Ordinary use is chat-native; persist only when the user requests it.

The run is fact-closed over the admitted Goal–Evidence Map. The Supervisor may organize or summarize
admitted facts, but must not add a new factual, quantitative, bibliographic, prevalence, benchmark,
usage, or comparative claim during synthesis. When authorized and decision-relevant, use Web retrieval
under the per-run boundary in [workflow](references/workflow.md) and open primary or authoritative
sources; memory and snippets are leads, not evidence. Apply the gate in
[scientific objects](references/contracts.md) before promotion and final packaging. Use it for record
access and workflow for Stage Value/finite attempts. Required independent Reviews remain mandatory.

## Six-block path

1. **Goal + Evidence Map:** freeze the question, decision boundary, evidence envelope, contradictions,
   resource limits, privacy, safety, and what would block ideation.
2. **Multi-strategy Generation:** use mechanism, falsifier/discriminator, and boundary/transfer lenses
   to produce normally 2–4 distinct Hypothesis Cards. Do not fill a failed producer's quota.
3. **Reflection + Deep Verification:** give each admitted candidate an independent Review Record;
   check evidence, nearest collisions, anti-stitching, alternatives, formal claims, feasibility,
   falsifiability, and the single killer objection.
4. **Proximity + Ranking (conditional):** compare only when at least two reviewed candidates remain
   and the result can change Evolution allocation or human presentation. A total order is unnecessary.
5. **Evolution + Fresh Reflection:** bind one exact objection to one material scientific change, keep
   the parent, and require a complete non-author fresh review before any descendant is promoted.
6. **Meta-review + Human Selection:** synthesize without adding scientific authority, preserve
   disagreement and workflow failures, present only independently eligible finalists, ask for the
   scientist's decision, and end the current run.

Use [workflow](references/workflow.md) for routing and legal exits, [temporary perspectives](references/roles.md)
for bounded delegation, [scientific objects](references/contracts.md) for readable returns, and
[safety and provenance](references/safety.md) throughout.

## Defaults and stops

- Normally 2–4 initial candidates, at most 3 concurrent subagents, and one Evolution round. Optional
  calls must change a decision under the Stage Value test; comparison remains decision-relevant only.
- One valid candidate may continue with an explicit diversity limitation; zero candidates stops.
- Valid siblings survive candidate-, review-, or descendant-local failure.
- Stop on a run-level safety, authorization, privacy, leakage, or shared-evidence boundary; no usable
  evidence anchor; exhausted budget; unavailable decisive expertise; or a required human decision.
- Block 6 is the endpoint. A later pass requires a new explicit user request and a new Block 1 boundary.

## Output boundary

Return a complete Decision Package: problem/evidence map; eligible primary and optional distinct
reserve, or the applicable no-finalist, unresolved-choice, repair-allocation, or workflow-failure
package; strongest support and objection; Reviewer-driven changes; predictions, falsifiers,
boundaries, nearest-work status, cheapest discrimination design, uncertainty, and the next human
decision. State shared facts and evidence once; remove literature retelling and workflow narration
that cannot change a decision.

When useful, prefix the optional fact-closed Executive Decision from `contracts.md`; the full package remains authoritative.

Before returning, audit every exact number, percentage, range, date, rank, count, benchmark,
prevalence/adoption statement, and named-source comparison. It must have an admitted source/location
binding or a visible non-factual provenance label such as `human-utility choice` or `placeholder`.
An unsupported decisive claim blocks promotion; a non-decisive unsupported detail is omitted from the
Decision Package rather than repaired from memory.

**Execution is not authorized by this Skill output.** Code, training, data collection, experiments,
external communication, repository mutation, or paper writing requires a separate user request and owner.
