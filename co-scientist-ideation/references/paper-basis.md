# Paper Basis and Adaptation Boundary

## Primary sources

- Gottweis, J. et al. *Accelerating scientific discovery with Co-Scientist*.
  **Nature 655**, 487–496 (2026). DOI: `10.1038/s41586-026-10644-y`.
  <https://www.nature.com/articles/s41586-026-10644-y>
- Supplementary Information, especially safety, agent pseudocode, and specialized-prompt notes.
  <https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-026-10644-y/MediaObjects/41586_2026_10644_MOESM1_ESM.pdf>
- Google Research's public system overview.
  <https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/>
- Official Codex Skill and subagent documentation.
  <https://learn.chatgpt.com/docs/build-skills>
  <https://learn.chatgpt.com/docs/agent-configuration/subagents>

## Scientific functions retained

This Skill preserves the paper's scientific functions in a bounded form:

- goal interpretation and evidence-grounded problem mapping;
- multi-strategy Generation of distinct hypotheses;
- Reflection, bidirectional criticism, deep verification, and nearest-collision checking;
- Proximity and bounded pairwise comparison when the decision needs them;
- objection-driven Evolution with parent preservation and fresh opposition;
- Meta-review-style synthesis and scientist-in-the-loop selection;
- safety checks at goal and candidate scope.

The unit of design is a scientific function, not a permanent Agent. A temporary Codex perspective may
apply several strategies, and the parent may perform work directly when independence is unnecessary.

## Deliberate bounded adaptation

- Default candidate volume is normally 2–4, not system-scale search.
- Comparison is conditional, qualitative, and allocation-oriented; no default rating or total order is needed.
- The distinguishing value is evidence-backed problem → competing explanations → independent killer
  objection → material repair → fresh Review → human decision.
- Readable scientific objects are primary. Formatting or packaging checks cannot determine scientific quality.
- Local candidate/review failures preserve valid siblings; only shared authorization, privacy, leakage,
  safety, or evidence contamination stops the whole run.
- Temporary context exists only inside the current task. Durable artifacts are user-requested.

## Protocol success versus scientific success

A coherent Skill structure and passing deterministic checks establish only that the intended
instructions, activation boundary, and file package are present. They do not establish novelty,
feasibility, causal truth, experimental effect, or research value. Those require real evidence,
independent scientific judgment, and eventually separately authorized experiments.

## Not reproduced or claimed

The Skill does not reproduce proprietary asynchronous infrastructure, dynamic compute allocation,
worker management, persistent context memory, tool APIs, candidate databases, queues, services,
large-scale tournaments, calibrated internal metrics, experiment execution, or a closed laboratory loop.
It does not claim the paper's performance numbers, discoveries, wet-lab results, or independence between
perspectives that share related models.

The correct description is: **a bounded Codex research-ideation Skill inspired by Co-Scientist's
scientific functions**, ending in a human decision package.

