# Readable Scientific Object Contracts

## Representation rule

Ordinary runs use readable Markdown, not a required machine schema. Models author scientific content
once. Each fact or decisive premise has one canonical evidence binding; do not repeat evidence unions.
A binding exposes provenance but does not prove support.

Classify each claim-use, not whole files, and use the narrowest authority when ambiguous:

| Record class | Authority |
|---|---|
| `SOURCE_EVIDENCE` | Admitted claim-use with source, scope, location, relation, and limitation; supports only itself. Checksums do not promote logs. |
| `PRACTICE_OBSERVATION` | Default for provenanced internal runs/logs; supports feasibility, not unmeasured literature, causal, or generalized claims. Admission upgrades only the measured claim-use. |
| `PRIOR_CANDIDATE` | Prior design object and collision lead; never evidence that its mechanism works. |
| `REVIEW_DISPOSITION` | Prior objection/comparison/no-repair as design/risk history, not truth. |
| `HUMAN_DECISION` | User scope, utility, budget, risk, or authorization; not empirical evidence. |
| `UNVERIFIED_NOTE` | Retrieval lead only; admit its source, then apply the gate below to exact/named-source claims. |

Access never upgrades authority; peer drafts stay hidden. Independent divergence withholds prior
formulas, rank, preference, and dispositions, or is labeled inheritance-aware. Root Review hides the
current author/generation lens, preference, rank, and same-candidate prior disposition; Comparator
keeps these blind fields.

## Quantitative and citation admission gate

Apply this gate to every scientific object and again to the final Decision Package.

- A reported factual claim containing an exact number, percentage, range, date, rank, count,
  benchmark value, prevalence/adoption/usage statement, or named-source comparison requires one
  admitted evidence row whose source identity, specific claim, and location support that exact detail.
- A citation attached to a nearby topic is insufficient. Wrong-source attribution, a search snippet,
  model memory, repeated agent agreement, or an unverified secondary retelling does not pass.
- A proposed threshold, sample size, resource cap, or expected effect is a Design choice unless the
  source actually reports it. Keep the existing `source-backed`, `pilot-calibrated`, `human-utility
  choice`, or `placeholder` label beside it.
- If an unsupported or mismatched claim is decisive, return `revise` or `insufficient evidence` and
  prohibit finalist use. If it is non-decisive, preserve it only in the originating object as an
  explicit unresolved claim; omit it from Supervisor synthesis.
- The Supervisor is fact-closed over admitted evidence. It may compress, order, and connect admitted
  facts without changing their scope, but it cannot introduce a new factual detail. A needed new fact
  must return to evidence admission before downstream use.

This gate audits provenance and claim–source alignment. It does not treat the presence of a citation
as proof, forbid clearly labeled hypotheses, or turn readable Markdown into a machine schema.

## 1. Goal–Evidence Map

```text
Research question
Why it matters
Observed or reported anchors
Direct supporting evidence
Contradictory or limiting evidence
Nearest established explanations and methods
Unresolved problem/gap and competing explanations
Resource and measurement envelope
Retrieval, date/corpus, safety, and privacy boundary
What would block Generation
Exit: advance / blocked, with reason
```

When binding downstream claims, use a compact evidence row:

```text
E# | source identity | specific claim | location/anchor |
relation: supports / contextualizes / contradicts / limits / unresolved | important limitation
```

Facts, interpretations, hypotheses, predictions, and design choices remain visibly distinct. One bad
citation invalidates its claim, not unrelated evidence. A local fabricated citation triggers a bounded
shared-evidence check; shared contamination is a whole-run stop.

## 2. Hypothesis Card

```text
Candidate ID and short title
Problem pressure and value
Claim type: general / causal-mechanistic
One explanatory spine
Nearest-work functional delta or honest unknown
Decisive assumptions
Predictions
Direct falsifier
Named alternatives and their different predictions
Boundary conditions and failure modes
Cheapest discrimination design
Key go/no-go thresholds with provenance, when used
Evidence anchors and unresolved claims
Resource and safety fit
```

For causal/mechanistic claims, include the intervention seam, affected entity/state, direction,
mediator/trajectory, appropriate control, wrong-reason explanation, and mechanism-targeting falsifier.
For transfers, include source principle, target pressure, structural correspondence, what is not
transferred, analogy-break boundary, target prediction/falsifier, and nearest target alternative.

Only for algorithmic, systems, formal, numerical, or operator-semantic claims, add a Constructive
Contract: object/state; invariant; update or propagation rule; complexity, memory, or precision
contract as applicable; proof obligation or minimum counterexample; and nearest implementation with
the exact functional delta. Do not impose this contract on ordinary biological, cognitive,
observational, or empirical claims.

Label each key go/no-go threshold exactly one of `source-backed`, `pilot-calibrated`, `human-utility
choice`, or `placeholder`. Keep the label beside the relevant threshold rather than in a separate
ledger. A `placeholder` may guide inquiry but cannot promote a finalist.

The Generator may state a proposed identity, base case, candidate case, or off condition in prose. It
does not declare formal/dimensional validity, novelty, Reviewer disposition, or ranking.

## 3. Review Record

```text
Review ID and Candidate ID
Reviewer independence statement
Verdict: continue / revise / reject / insufficient evidence
Problem/framing assessment
Strongest support case
Strongest opposition case
Decisive assumptions with local evidence status
Nearest collision or functional equivalent
Main alternative explanations
Formal/dimensional/operator or causal check when applicable
Killer objection
Repairable scientific fields
Cheapest decisive test
What evidence would change the verdict
```

`continue` means coherent and worth discriminating, not true or novel. `revise` must bind one exact
killer objection to named repairable scientific fields. `reject` records the decisive failure.
`insufficient evidence` names the missing authority. A Review is admitted independently of sibling
Reviews. The Reviewer, not the Generator, owns formal and dimensional validity.

## 4. Comparison Record

```text
Pair
Why this comparison can change a decision
Proximity: duplicate / compatible variant / distinct
Shared explanatory core and material differences
Hard-gate status
Decision in each order when reversal is used
Normalized result: left / right / tie / reject_both / insufficient_evidence / order_unstable
Decisive reasons and evidence gaps
What would change the result
Allocation: evolve / retain / reject / ask human
```

Do not duplicate full cards, Reviews, or evidence inside the comparison. No result establishes
scientific truth or requires a total order.

## 5. Evolution Record

### Descendant record

```text
Descendant ID and Parent ID
Authoritative parent Review
Exact killer objection
Why it blocks the parent
Evolution operation in ordinary language
Changed scientific fields
Revised spine, assumptions, predictions, falsifier, boundaries, or discriminator as applicable
Why the change could address the objection
What was preserved
What must receive fresh review
Fresh independent Review and outcome, once it exists
```

An Evolution claim requires a material scientific change and a complete non-author fresh Review.
Parent and descendant remain separate. A diverged descendant's complete fresh Block 3 Review is its
normal Review.

### No-repair record

```text
Parent and authoritative Review
Exact killer objection
Why it is fatal, not repairable, or not worth current budget
Disposition: reject / retain-as-unresolved
```

No descendant or fresh Review exists, and completed Evolution is not claimed.

### Descendant-review failure

```text
Parent, descendant, exact objection, and material change
Fresh Review failure or unavailable authority
Descendant status: unvalidated; comparison/finalist use prohibited
Parent status: unchanged
```

## 6. Decision Package

```text
Research question and why it matters
Evidence-grounded problem map and limits
Primary hypothesis and optional distinct reserve, when resolved and eligible
Every eligible unranked candidate and missing decision variable, when final selection is unresolved
Unranked repair-target alternatives, when Evolution allocation is unresolved
No-finalist or workflow-failure account, when applicable
One explanatory spine and nearest-work/novelty status
Strongest support and killer objection
Independent Review and Reviewer-driven change
Evolution lineage and fresh-review outcome, if completed
Predictions, direct falsifiers, alternatives, boundaries, and failure modes
Cheapest discrimination design
Key go/no-go thresholds and provenance, when used
Rejected candidates and decisive reasons
Unresolved evidence, minority views, and useful resource summary
Next human decision
Execution is not authorized by this Skill output.
```

Optional **Executive Decision** contains only: outcome, eligible/unresolved set, controlling
support/objection, and next human decision. No other field enters this fact-closed projection. It
creates no evidence, verdict, rank, confidence, threshold, authority, call, or file; the full package
remains authoritative.

## Admission and authority matrix

| Object | Authority needed for downstream scientific use |
|---|---|
| evidence claim | eligible source or explicit unresolved/internal provenance |
| root candidate | complete readable card; then independent Block 3 Review for finalist use |
| root primary/reserve | current admitted independent `continue` Review |
| descendant | material parent-bound change plus complete non-author fresh Review |
| descendant primary/reserve | complete fresh independent `continue` Review covering all Block 3 gates |
| comparison | authoritative Reviews for both candidates and a decision-relevant pair |
| Supervisor synthesis | presentation only; grants no new scientific authority |

`revise`, `reject`, `insufficient evidence`, unreviewed, unvalidated, and retain-as-unresolved objects
cannot be primary or reserve. A local failure leaves valid siblings available. A run-level safety,
authorization, privacy, privileged-information, leakage, or shared-evidence stop prevents downstream use.

## Scratch and persistence

The parent may keep transient notes in the current task. Persist only a user-requested artifact. Do
not create a candidate store, lineage database, cross-run memory, task queue, or execution record as a
scientific gate. Optional formatting checks can verify a user-requested export, but they cannot decide
scientific quality or block a readable human result.
