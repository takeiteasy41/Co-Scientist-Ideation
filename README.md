# Co-Scientist Ideation

An explicit Codex Skill for turning an open research direction, observation, or contradiction into a
bounded and evidence-grounded decision package. It keeps mechanisms, evidence, criticism,
uncertainty, and the researcher’s final choice visibly separate.

[Chinese documentation](README-Chinese.md)

## What it is for

Use this Skill when you already have a research direction, observation, anomaly, or question and need
to decide what is most worth distinguishing next. It is useful for:

- mapping a question, evidence, contradictions, constraints, privacy boundaries, and stopping rules;
- generating a small set of mechanistically distinct and falsifiable hypotheses;
- checking evidence bindings, nearby work, alternative explanations, confounders, and failure modes;
- turning one specific killer objection into a substantive scientific revision;
- proposing the lowest-cost discriminator before code, training, experiments, or data collection; and
- preparing a comparable Decision Package for a researcher to select.

It is not a general chatbot, a literature-search replacement, an autonomous laboratory, or a guarantee
of novelty, correctness, or publication.

## Six-stage workflow

    Goal + Evidence Map
      → Multi-strategy Generation
      → Independent Review
      → Conditional Comparison
      → Objection-driven Evolution + fresh review
      → Decision Package + Human Selection

| Stage | Core work | Main output |
|---|---|---|
| 1. Goal + Evidence Map | Freeze the question, evidence boundary, contradictions, resources, privacy, and stopping conditions. | Goal–Evidence Map |
| 2. Multi-strategy Generation | Produce a few candidates that differ in mechanism, not just wording. | Hypothesis Cards |
| 3. Independent Review | Check evidence use, nearby work, alternatives, falsifiability, feasibility, and killer objections. | Independent Review Records |
| 4. Conditional Comparison | Compare candidates only when it can change revision effort or human choice. | Comparison Record, or an explicit skip |
| 5. Evolution + fresh review | Bind a substantive revision to one exact objection and have a non-author review the descendant. | Evolution lineage and fresh Review |
| 6. Decision Package + Human Selection | Summarize support, objections, uncertainty, failures, and the cheapest next discriminator for the researcher. | Decision Package |

The workflow does not force a final ranking. No qualified finalist, insufficient evidence, or a
decision that requires human values are valid outcomes.

## Design principles

- **Evidence binding.** Facts, interpretations, hypotheses, predictions, and design choices remain
  distinct. Exact numbers, dates, rankings, and named-source comparisons must be tied to a source and
  location that supports that specific statement. Search snippets, memory, and role consensus are
  discovery leads, not evidence.
- **Mechanism distinction.** Each candidate states one explanatory line, its nearest functional
  precedent, the key difference, an alternative explanation, and predictions that could distinguish
  them.
- **Independent criticism.** A candidate’s author does not review it. Evolution descendants receive a
  complete fresh review from a non-author role. This is process separation, not human or statistical
  independence.
- **Objection-driven revision.** Evolution must answer one exact killer objection by changing
  scientific content such as the mechanism, key assumption, prediction, falsifier, boundary, or
  discriminator.
- **Bounded resources.** Candidate count, temporary perspectives, retrieval, and Evolution remain
  finite. Optional work is used only when it can change a scientific decision.
- **Human control.** The Skill stops at a Decision Package. Code, training, experiments, data
  collection, external communication, repository changes, and paper writing require separate
  authorization.

## Installation

Copy the complete co-scientist-ideation/ directory into a supported Skill root. Do not copy the
repository root or the evaluation method into a Skill root.

macOS / Linux:

```bash
git clone https://github.com/takeiteasy41/Co-Scientist-Ideation.git
mkdir -p "$HOME/.agents/skills"
cp -R Co-Scientist-Ideation/co-scientist-ideation "$HOME/.agents/skills/"
```

Windows PowerShell:

```powershell
git clone https://github.com/takeiteasy41/Co-Scientist-Ideation.git
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse ".\Co-Scientist-Ideation\co-scientist-ideation" "$HOME\.agents\skills\co-scientist-ideation"
```

If the destination already contains a Skill with the same name, confirm or back it up before copying
so that two packages are not silently merged. For a project-scoped installation, copy the complete
directory to <project>/.agents/skills/ instead.

The public evaluation method is optional and is not needed for installation or runtime. It is
documented under [evaluation/public-method](evaluation/public-method/README.md).

## Usage

In a new Codex task, invoke the Skill explicitly and provide the scientific decision you need to
make:

```text
$co-scientist-ideation

Research goal: <what you want to explain, compare, or discover>
Evidence and retrieval boundary: <available materials, databases, papers, or time range>
Current scientific decision: <what this result must help you decide>
Web: <which public sources may be searched, or whether to stay offline>
Privacy: <unpublished, proprietary, personal, or sensitive details that must not enter queries>
Resources: <data, measurements, compute, time, cost, and expertise available>
Expected output: Decision Package
```

The Skill asks for a human decision first when missing information would change scientific validity,
privacy, authorization, cost, or scope.

## Returned package

A complete result can include:

- Goal–Evidence Map;
- Hypothesis Cards;
- independent Review Records for each candidate;
- a Comparison Record when comparison has decision value;
- an Evolution parent–descendant lineage and fresh Review;
- strongest support, killer objection, alternatives, and nearest-work status;
- discriminating predictions, direct falsifiers, boundaries, and failure modes;
- a lowest-cost discriminator with source or design provenance for key thresholds;
- rejected candidates, unresolved evidence, minority views, and process limitations;
- qualified finalists, an unranked human choice set, or an honest no-finalist result; and
- the next decision required from the researcher.

In a Review, continue means that a candidate is coherent and worth testing. It does not mean that the
candidate is proven, novel, experimentally validated, or ready for publication.

## Web, privacy, and execution control

Web retrieval is run-scoped. It is used only when authorized and decision-relevant, with preference
for primary papers, official datasets, standards, documentation, or original repositories. Search
snippets are discovery aids; support, contradiction, limitations, negative evidence, and unresolved
claims remain visible after source checking.

Unpublished hypotheses, exact private numbers, identifying information, and collaborator details do
not enter Web queries by default. Queries use an abstract formulation unless the researcher
explicitly authorizes more detail. Local files and data are not uploaded to external services without
permission.

Automatic activation is disabled by design. The package keeps
policy.allow_implicit_invocation: false, so ordinary tasks are unaffected until the researcher types
$co-scientist-ideation.

## Package structure

- co-scientist-ideation/SKILL.md: entry point, trigger boundary, and overall contract.
- co-scientist-ideation/agents/openai.yaml: display metadata and explicit invocation policy.
- co-scientist-ideation/references/workflow.md: routing, stopping conditions, and valid exits.
- co-scientist-ideation/references/contracts.md: scientific objects, evidence admission, and
  Decision Package contract.
- co-scientist-ideation/references/roles.md: temporary scientific perspectives and independence
  boundaries.
- co-scientist-ideation/references/safety.md: source, privacy, safety, and human-control guidance.
- co-scientist-ideation/references/localization.md: activation and host-local adaptation.
- co-scientist-ideation/references/paper-basis.md: source basis and bounded adaptation.
- co-scientist-ideation/scripts/: package validation.
- co-scientist-ideation/tests/: behavior and structural checks.

## Tests and evaluation

We ran a small AI-only, fixed-task exploratory paired evaluation to observe this workflow under a
controlled evidence envelope. It is provided for context, not as a claim of universal effectiveness.

### Method

- Four fixed tasks: two systems/formal tasks and two non-systems tasks.
- Each task supplied five earlier, verified papers to both generation arms: twenty visible papers in
  total.
- Each task also had one later hidden reference paper, four hidden references in total. Their
  identities and contents were withheld from the generation arms and primary reviewers.
- The hidden references were used only after review lock for a non-voting mechanism-family comparison.
- The two generation arms were Co-Scientist and a high-quality Generic prompt.
- Each task had three paired generations, producing twelve anonymous pairs.
- Each pair had three eligible AI reviewer decisions, producing thirty-six nested decisions.
- The task was the primary analysis unit, with equal task weight.

### Observed descriptive endpoint

| Quantity | Result |
|---|---:|
| Reviewer directions toward Co-Scientist | 31/36 |
| Pair majorities toward Co-Scientist | 11/12 |
| Task-equalized score | 0.861111 |
| Co-Scientist canonical critical failures | 1 |
| Generic canonical critical failures | 0 |
| Co/Generic generation-request ratio | approximately 3.83× |
| Co/Generic mean parent wall-time ratio | approximately 1.99× |

The directional numbers favored Co-Scientist in this panel, but the result was not an unconditional
win. One Co-Scientist output contained a substantive source-use error, one pair majority favored
Generic, and the predeclared no-worse-critical-failure gate did not pass. The terminal interpretation
is a heterogeneous trade-off: a stronger anonymous preference signal in these tasks accompanied
greater request and time costs.

Reviewer choices were nested within pairs and tasks, not thirty-six independent scientific
replicates. The endpoint is a recovery from frozen records, not an independent replication. A hidden
reference paper is a historical mechanism used for reconstruction/alignment; it is not scientific
truth, a unique correct answer, or proof of de-novo discovery. Cost ratios are local descriptive
records, not causal efficiency or ROI estimates.

The evaluation does not establish generic superiority, human preference, confirmatory efficacy,
scientific truth, true novelty, cross-domain generalization, or deployment ROI. The public evaluation
method package documents the metric layers, aggregation, schema, deterministic validators, Generic
capability envelope, and known weaknesses for developer review.

### Generic capability envelope

The retained Generic prompts declared and restricted the research capability envelope to:

- research-ideation — no authoritative upstream GitHub source was confirmed for the exact local Skill,
  so no download link is provided;
- [hypothesis-generation](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/hypothesis-generation);
- [scientific-brainstorming](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/scientific-brainstorming);
- [literature-review](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/literature-review); and
- a host-bundled read-only PDF capability for the supplied paper packet.

The Generic arm was also constrained to no network retrieval, no project writes, and no subagents.
These are evaluation-run controls, not a global restriction on this Skill’s authorized, run-scoped
Web retrieval. The retained runtime receipts do not record a positive per-request list of Skill
invocations, so the evaluation should not be read as proof that every request used every named Skill.

## Scientific basis and official references

This Skill adapts scientific functions described in the Co-Scientist work into a bounded, task-local
workflow:

- Gottweis et al., [Accelerating scientific discovery with Co-Scientist](https://www.nature.com/articles/s41586-026-10644-y),
  Nature, DOI 10.1038/s41586-026-10644-y.
- [Supplementary Information](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-026-10644-y/MediaObjects/41586_2026_10644_MOESM1_ESM.pdf).
- Google Research, [Accelerating scientific breakthroughs with an AI co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/).
- OpenAI, [Build skills](https://learn.chatgpt.com/docs/build-skills) and
  [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

Results, architecture, and experimental outcomes from those sources do not automatically transfer to
this Skill.

## License

Unless otherwise stated, original content supplied by the repository owner is licensed under the
[Apache License 2.0](LICENSE). Third-party papers, linked resources, and local research materials
that are not included in this repository remain under their own terms and are not relicensed here.
