# Co-Scientist Ideation: Public Evaluation Protocol

This protocol is the public method description for comparing a structured scientific-ideation
workflow with a strong general prompt. It is written for inspection and improvement. It is not an
experiment launch plan, a claim of universal superiority, or a release history.

## 1. Scope and claim contract

The method evaluates the quality of a research decision package under a frozen task and evidence
envelope. The relevant claims are separate:

| Claim family | Observable | Falsifier | Evidence tier |
|---|---|---|---|
| Decision usefulness | A researcher can identify the next meaningful discriminator. | The package does not change or clarify a decision. | Exploratory |
| Evidence grounding | Facts and quantitative claims are supported by admitted sources. | Source misuse, fabricated evidence, or unsupported decisive detail. | Exploratory / guardrail |
| Mechanism distinction | Candidates differ in mechanism and predicted observations. | Candidates are synonyms or share the same decisive prediction. | Exploratory |
| Falsifiability and controls | The package states rival explanations, falsifiers, and matched controls. | No outcome would weaken the central claim. | Exploratory |
| Honest stopping | The workflow abstains when evidence or authorization is insufficient. | It forces a finalist or supplies missing evidence from memory. | Guardrail |
| Human decision readiness | Qualified reviewers find the package actionable and bounded. | Reviewers cannot identify a safe, feasible next step. | Future human endpoint |
| Resource trade-off | Quality is reported together with actual requests and time. | Cost is inferred only from logical loop counts or omitted when unfavorable. | Descriptive |

One favorable metric does not support the other claim families. A workflow check is not scientific
success, and a reviewer preference is not proof of a scientific hypothesis.

## 2. Completed exploratory panel

The completed comparison used:

- four fixed tasks: two systems/formal tasks and two non-systems tasks;
- five earlier, verified visible papers per task, twenty visible papers total;
- one later hidden reference paper per task, four hidden references total;
- two generation arms: Co-Scientist and a high-quality Generic prompt;
- three paired generations per task, twelve anonymous pairs;
- three eligible AI reviewer decisions per pair, thirty-six nested decisions;
- task as the primary analysis unit, with equal weight across tasks;
- anonymous A/B presentation before reviewer choice;
- hidden-reference family comparison after review lock and outside the voting endpoint.

The visible packet was the complete evidence envelope for each generation. Hidden references were not
generation inputs or primary reviewer labels. They represent historical mechanisms for an alignment
diagnostic; they are not ground truth.

## 3. Generic capability envelope

The Generic arm was not a no-Skill or deliberately weak baseline. Its retained prompts declared and
restricted the following research capabilities:

1. research-ideation;
2. hypothesis-generation;
3. scientific-brainstorming;
4. literature-review.

The prompts also declared a host-bundled read-only PDF capability for the supplied paper packet.
Network retrieval, project writes, collaboration, and subagents were forbidden for this comparison.

The declared capability sources that could be confirmed are:

- [hypothesis-generation](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/hypothesis-generation)
- [scientific-brainstorming](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/scientific-brainstorming)
- [literature-review](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/literature-review)

No authoritative GitHub source was confirmed for the exact local research-ideation Skill. Third-party
mirrors were not treated as upstream sources. The PDF capability is host-bundled and is not included
in this repository.

The retained runtime receipts do not record a positive list of Skill invocations for each request.
The method therefore reports a declared/allowed capability envelope, not proof that every request
used every named Skill. A future per-Skill causal claim requires an auditable, privacy-safe capability
ledger.

## 4. Metric layers

### 4.1 Primary current endpoint

Each anonymous pair receives three eligible AI reviewer choices: A, B, or TIE. The pair score maps
the choice toward the Co-Scientist arm to 1, toward Generic to 0, and TIE to 0.5. Reviewer choices
are averaged within pair, pairs within task, and task means across the four tasks with equal weight.

This produces a task-equalized paired-preference endpoint. It is descriptive and exploratory.

### 4.2 Epistemic guardrails

A reviewer can mark canonical failures including:

- fabricated evidence;
- source misuse;
- a reversed or ignored confound;
- an unfalsifiable central claim;
- an unbounded action without a human gate; and
- false certainty under missing evidence.

Critical failure counts travel with the endpoint. A preference direction cannot erase an integrity
failure. Correct no-finalist, insufficient-evidence, and human-input requests are valid outcomes.

### 4.3 Diagnostic dimensions

The strict review record keeps eight secondary dimensions:

1. problem framing and decision focus;
2. evidence grounding and provenance;
3. assumption identifiability and confounding;
4. competing explanations and counterexamples;
5. predictions and falsifiability;
6. experiment control and failure design;
7. uncertainty boundary and honest stop;
8. human decision readiness.

Scores from 1 to 5 explain a primary choice; they do not mechanically determine it. Missing evidence
caps confidence and should be represented explicitly.

### 4.4 Hidden-reference alignment

After primary reviews are locked, a curator may compare the generated mechanism family with the hidden
historical reference. This is a reconstruction/alignment diagnostic. It is not a vote, truth label,
novelty proof, or claim that the target mechanism is uniquely correct.

Open-ended tasks have no hidden reference. A stronger but different idea may be valuable even if it
does not align with a historical target.

### 4.5 Resource metrics

Report actual, not planned, quantities where available:

- model, tool, or API requests;
- token usage;
- retries and cache hits;
- wall time;
- output length;
- human review minutes;
- valid candidate count;
- no-finalist outcomes;
- source-use and other critical failures.

The cost summary is a study-level non-causal description. It is not a return-on-investment estimate.

## 5. Fairness and controls

A future claimable comparison should freeze:

- common model, revision, decoding, context limit, and evidence envelope;
- a strong Generic baseline rather than a weak straw prompt;
- a structured single-agent arm to separate explicit structure from role separation;
- matched-request-budget and natural-process views;
- anonymous arm labels and balanced display order;
- target withholding until review lock;
- qualified-human blind review for open-ended quality;
- correct-stopping controls;
- actual request and cost accounting.

The reviewer model, prompt, and assignment policy must be recorded. Shared model families weaken
independence and should be disclosed.

## 6. Paper search and reference selection

For known-target reconstruction, selection follows this order:

1. freeze the claim, task stratum, evidence cutoff, target-publication window, and exclusion rules;
2. search multiple authoritative scholarly sources;
3. verify bibliographic identity and claim support from opened records;
4. select a primary paper with a clear central mechanism and enough earlier evidence;
5. build the visible packet from earlier sources without target-answer material;
6. scan prompts, metadata, filenames, manifests, and full text for target leakage;
7. seal packet bytes and hashes before generation;
8. keep target identity and mapping hidden until the task is retired.

Search snippets and model memory are discovery leads. A source becomes evidence only after the relevant
passage, scope, relation, and limitation are checked. Exact private queries may reveal a target and
remain outside the public package.

## 7. Current endpoint, limitations, and known weaknesses

The current recorded endpoint is:

- 31/36 reviewer directions toward Co-Scientist;
- 11/12 pair majorities toward Co-Scientist;
- task-equalized score 0.861111;
- one Co-Scientist canonical critical failure;
- zero Generic canonical critical failures;
- one pair majority toward Generic;
- approximately 3.83 times the generation requests for Co-Scientist;
- approximately 1.99 times the mean parent wall time for Co-Scientist.

The no-worse-critical-failure gate did not pass. The terminal interpretation is a heterogeneous
AI-only exploratory trade-off, not an unconditional win.

Limitations:

- reviewer decisions are nested and not independent scientific replicates;
- the panel contains four fixed tasks;
- the endpoint is a recovery from frozen records, not an independent replication;
- hidden-reference alignment can reward reconstruction rather than novelty;
- no human preference endpoint is present;
- the incremental causal effect of role separation is not identified;
- cost ratios are descriptive, not causal efficiency or ROI;
- public runtime receipts do not record per-request Generic Skill invocations;
- the retained local closure is not a complete rerun package;
- public-paper pretraining exposure cannot be proved absent.

## 8. Reproduction boundary

The public package reproduces schema validation, synthetic review admission, and explicit cost
calculation without network, model, PDF, or corpus access.

It does not reproduce the historical model requests or expose:

- hidden targets;
- exact private prompts or queries;
- raw generated packages;
- reviewer assignments or arm keys;
- downloaded paper files;
- local runtime and custody receipts.

This boundary is deliberate: a public method should be inspectable without turning a hidden evaluation
into a leaked answer set.

## 9. Contribution hooks

Useful improvements include:

- stronger human-centered endpoints;
- larger and more diverse task panels;
- role-ablation and matched-budget designs;
- independent reviewer calibration;
- per-request capability logging with privacy protection;
- tests for target leakage and source misuse;
- uncertainty and practical-significance reporting;
- better correct-abstention controls; and
- cost measures that reflect researcher time as well as model requests.
