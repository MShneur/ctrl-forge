# Evidence-Competitive Decisions

Use this rule for consequential product, architecture, implementation, research, dependency, and operational questions with multiple plausible answers.

## Rule

Do not narrow viable choices based only on persuasive arguments, apparent elegance, authority, familiarity, or consensus. Before eliminating plausible candidates, determine whether a proportionate test, prototype, benchmark, adoption check, or failure-injection exercise can distinguish them.

A working candidate must not be discarded merely because an untested alternative sounds better.

## Required process

1. Define the decision and measurable success criteria.
2. Preserve at least two viable candidates where practical.
3. Gather official upstream information and evidence from real deployments.
4. Include relevant user evidence without treating community comments as a representative survey.
5. Obtain independent proposals from materially different expert approaches.
6. Include one outside-frame alternative.
7. Declare evaluation weights before seeing results.
8. Identify and run the cheapest useful discriminating tests when feasible.
9. Cross-examine the strongest version of each surviving candidate.
10. Record rejected options, negative results, unresolved dissent, and verification limits.
11. Select the strongest supported option and state what evidence would reverse the decision.

## Evidence preference

Prefer, in order:

1. reproducible tests in the target project;
2. comparable production evidence;
3. official specifications, documentation, changelogs, and maintained examples;
4. issue and migration patterns;
5. qualitative user reports;
6. expert inference;
7. untested ideas.

Untested ideas remain experimental and cannot silently outrank stronger evidence.

## Suggested tests

Depending on the project, use:

- CI matrices;
- isolated proofs of concept;
- compatibility fixtures;
- CPU, memory, battery, bundle-size, and latency measurements;
- restart and failure injection;
- hostile-input and metamorphic tests;
- deterministic replay;
- artifact comparison;
- or shadow/canary evaluation.

Tests must be capable of changing the decision. Ceremonial tests do not satisfy this rule.

## Minimum decision record

Record the question, candidates, evidence, competing arguments, outside-frame option, tests, measurements, rejected choices, recommendation, minority position, verification limits, and smallest safe next action.
