# Activation and Local Adaptation

## Two-layer activation boundary

Skill discovery and the internal Trigger gate enforce the same boundary.

| User request | Activate? | Owner |
|---|---:|---|
| `$co-scientist-ideation` followed by a research goal | Yes | This Skill |
| "像 Co-Scientist 一样让多个科研角色提出并筛选假设" | Yes | This Skill |
| "让多个 AI 科研专家辩论并挑出可验证的研究方向" | Yes | This Skill |
| "Codex 做我的科研搭档，帮我想点子并做多角色审查" | Yes | This Skill |
| "用 subagents 实现这个 React 功能" | No | Normal software workflow |
| "spawn 三个 agents review PR" | No | Code-review workflow |
| "并行调试训练脚本" | No | `diagnose` or normal debugging |
| "总结这篇 Co-Scientist 论文" | No | Paper reader or lookup owner |
| "开放式帮我想几个选题" without role-separated screening | No | `scientific-brainstorming` |
| "根据这组异常结果给出可检验假设" | No | `hypothesis-generation` |
| "把方向收敛成课题计划" | No | `research-ideation` |
| "冻结 baseline、split、seed 和统计方案" | No | `ml-experiment-design` |

Mentioning `Co-Scientist`, `agent`, `subagent`, AI, research, or hypothesis separately is
insufficient. The intent must combine scientific ideation with an explicit request to run or imitate
Co-Scientist or to use role-separated generation and screening. If this Skill loads on a negative
case, exit before reading role prompts, retrieving, delegating, or writing.

## Local Codex execution

- The parent Codex owns requirements, authorization, admission, decisions, and the final response.
- Temporary subagents receive bounded read-only scientific tasks and return concise Markdown. They do
  not edit shared files or become a permanent team.
- Use at most three concurrent subagents. Reuse slots across blocks and disclose unavailable
  independence instead of inventing consensus.
- Subagents inherit the parent's sandbox and permissions. A blocked perspective does not broaden them.
- Do not create global custom-Agent configuration or preload every adjacent research Skill.

## Workspace hygiene

- Ordinary ideation remains in chat. Create a durable artifact only when the user requests one or an
  approved research-artifact location already exists.
- Do not create repository-local work directories, state files, candidate stores, or reports merely
  because the Skill was loaded.
- Never read credentials, API keys, cookies, private browser profiles, or unrelated workspace files.
- Before web search, decide whether unpublished details may appear in queries; default to abstracted terms.

## Domain-neutral adaptation

Apply only the checks the goal needs.

- Empirical/data work: provenance, sampling/split unit, leakage/duplicates, baseline fairness,
  versions/seeds where relevant, metrics, uncertainty, resources, and failure taxonomy.
- Computational/physical/biological work: units, entities, boundary conditions, independent units,
  database provenance, formal checks, controls, and simulation-versus-empirical boundary.
- Agent/tool research: distinguish a proposed logical step from an actual model/tool request and keep
  evaluator, environment, request budget, and success/failure assumptions explicit at design level.

## Adjacent skills

- Exact record lookup: `paper-lookup`
- Coordinated search: `nature-academic-search`
- Systematic synthesis: `literature-review`
- Open divergence without role-separated review: `scientific-brainstorming`
- Observation-driven hypotheses: `hypothesis-generation`
- Project framing: `research-ideation`
- Frozen ML experiment contract: `ml-experiment-design`
- Completed-run statistics: `results-analysis`
- Manuscript drafting: `ml-paper-writing` or `nature-writing`

Load an adjacent owner only when the current block requires its artifact. Moving from the Decision
Package into experiments, code, external communication, or writing requires a new user request.

