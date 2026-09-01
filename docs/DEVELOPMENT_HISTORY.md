# Development History

This is the durable development record for the current Skill. It keeps decisions and failure lessons
that matter for future maintenance while omitting machine paths, task/session identifiers, raw prompts,
traces, and superseded process documents.

## 2026-08-27 — scientific workflow became the unit of design

The project moved from a loose collection of research-agent ideas to a bounded six-block design:

1. Goal + Evidence Map;
2. Multi-strategy Generation;
3. Reflection + Deep Verification;
4. conditional Proximity + Ranking;
5. objection-driven Evolution + fresh review;
6. Meta-review + Human Selection.

The important architectural choice was to represent scientific functions with temporary perspectives
rather than permanent services. Readable scientific objects—Hypothesis Cards, Review Records,
Evolution Records and the Decision Package—became the interfaces between stages. This kept the design
usable inside an ordinary Codex task and made stopping conditions visible.

## 1.6-dev — executable six-block baseline

The first cohesive package established the trigger gate, role prompts, workflow, safety guidance,
scientific object contracts, tests, and a structural validator. It also fixed the long-term scope:
small candidate sets, bounded subagent concurrency, one normal Evolution round, and an endpoint owned
by the researcher.

The main lesson was that workflow completeness and scientific quality are different. A package can be
structurally valid while its claims, evidence or candidate distinctions remain weak; versions
1.7–1.9 therefore strengthened admission and observable behavior instead of adding infrastructure.

## 1.7-rc1 — evidence admission and fact closure

Version 1.7 introduced an exact quantitative/citation admission gate and made the Supervisor fact-closed
over admitted evidence. Numbers, dates, rankings, prevalence statements and named-source comparisons
must carry a source/location binding or a visible non-factual provenance label. Unsupported decisive
claims block promotion; non-decisive unsupported details are omitted.

Fresh forward cases exposed a recurring failure mode: a relevant-looking source or search snippet can
still fail to support the attached claim. The correction was an evidence-use contract, not broader
retrieval or more confident prose. The version passed its legacy, regression, structural and bounded
forward checks while retaining explicit-only invocation.

## 1.8-rc1 — operational contracts without a runtime platform

Version 1.8 added four narrow operational seams:

- a Stage Value test for optional work;
- claim-use record authority and role-specific access overlays;
- finite attempt and failure-lineage accounting;
- an optional, fact-closed Executive Decision projection.

These changes clarified when to retrieve, compare, repair or stop without adding a runner, queue,
database or persistent memory. A first Executive Decision behavior render included an extra admitted
field; a fresh replacement test established the narrower four-field projection. This became a useful
maintenance rule: when a real behavioral failure appears, replace the affected version through an
audited sibling change rather than silently relaxing the test.

## 1.9-rc1 — run-scoped retrieval and domain-neutral discrimination

Version 1.9 was created as a sibling of frozen 1.8. It changed seven leaves and preserved six leaves
byte-for-byte. Two user-facing issues drove the change:

1. Web access needed to be available when a run authorizes it, while source admission, privacy and
   human control remain intact.
2. Checks for complex scientific systems needed to distinguish multiple components without importing
   assumptions from one particular field.

The resulting contract inventories the permitted corpus or Web boundary per run, opens primary or
authoritative sources before claim use, and treats snippets and memory as leads. Multi-component work
uses a general bottleneck → matched isolation → local falsifier pattern; domain-specific examples
select relevant checks but do not define the scientific answer.

The package passed `16/16` behavior/regression tests, the structural validator, the official quick
validator, and one bounded real Web-authorized forward task. The task ended with an accepted no-finalist
Decision Package, showing that evidence-grounded stopping remained available after network retrieval.

## Exploratory comparative evaluation

The final retained endpoint was recovered on 2026-08-31. Across four fixed tasks, twelve anonymous
pairs and three AI reviewer decisions per pair, 31/36 effective directions and 11/12 pair majorities
favored Co-Scientist; the task-equalized score was `0.861111`.

The endpoint was classified `AI_ONLY_EXPLORATORY_HETEROGENEOUS`, not local advantage, because one
Co-Scientist package received a substantive `SOURCE_MISUSE` failure while Generic received none in the
effective panel. One pair majority also favored Generic. This negative result is retained as a design
constraint: richer scientific structure must not trade away source discipline, and narrow actionable
comparisons can sometimes be preferable.

## Public-release and personal-promotion decision

The final public package keeps the validated 12-file payload and replaces only the private release
manifest with a portable receipt. Automatic activation remains disabled. The official portable user
Skill location and the current host-specific personal location are both documented without treating
them as interchangeable standards.

Public source, local endpoint-recomputation evidence, and finalization/deployment receipts are separate
surfaces. Public documentation does not claim that a particular machine has installed the Skill;
machine-specific promotion and discovery evidence stays in ignored internal custody.

## Durable lessons

- Freeze scientific and operational boundaries before implementation.
- Use the smallest test that observes the changed seam, then broaden only for shared contracts.
- A no-finalist result can be a successful workflow outcome.
- Retrieval availability and evidence admission are separate controls.
- Temporary cognitive roles do not require a permanent multi-agent platform.
- Hash receipts must preserve relative-path meaning and avoid self-containing tree hashes.
- Evaluation claims must use the declared aggregation unit and retain adverse findings.
- Installation scope is part of behavior: project-local discovery does not prove cross-project
  personal discovery.
