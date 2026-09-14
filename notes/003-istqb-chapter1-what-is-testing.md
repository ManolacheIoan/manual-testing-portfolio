# ISTQB Foundation Level — Chapter 1: What Is Testing?

Notes from Chapter 1 of ISTQB Foundation Level V4.0 course material.

## Testing vs. Test Execution

Testing is a full process made up of many activities — execution is
only one of them (also includes planning, analysis, design, closure).

## Static vs. Dynamic Testing

- **Dynamic testing** — involves actually executing the
  component/system under test
- **Static testing** — does NOT involve execution (e.g. reviews,
  static analysis of code/documents)

## Verification vs. Validation

- **Verification** — "Are we building the product right?" (does it
  meet specified requirements)
- **Validation** — "Are we building the right product?" (does it meet
  the actual needs of stakeholders/users)

## Testing vs. Quality Assurance (QA)

Testing and QA are NOT the same thing. Testing is a form of
**Quality Control (QC)**.

| | QA | Testing |
|---|---|---|
| Focus | Process-oriented, preventive | Product-oriented, corrective |
| Aim | Improve processes | Achieve appropriate quality levels |
| Responsibility | Everyone on the project | Primarily testing teams |
| Belief | Good process → good product | Detect and fix defects |

## Errors, Defects, Failures, Root Causes

Chain: **Root Cause → Error/Mistake → Defect (fault/bug) → Failure**

- A defect does not always cause a failure (code with a bug that's
  never executed produces no failure)
- Root Cause Analysis identifies the fundamental reason behind a
  problem, to prevent similar defects/failures recurring — not just
  fix the symptom

Common causes of human error: time pressure, fatigue, lack of
training, complex work products/processes/infrastructure.

Defects can also originate from environmental conditions (e.g.
radiation/EM fields affecting firmware), not just human error.

## The 7 Testing Principles

1. **Testing shows the presence of defects, not their absence** —
   testing reduces the probability of undiscovered defects, but can
   never prove the system is defect-free.
2. **Exhaustive testing is impossible** — except in trivial cases; use
   risk-based prioritization instead of trying to test everything.
3. **Early testing saves time and money** — defects caught early don't
   cascade into derived work products; start static AND dynamic
   testing as early as possible.
4. **Defects cluster together** — a small number of components
   usually account for most defects (Pareto principle) — useful input
   for risk-based testing.
5. **Tests wear out (pesticide paradox)** — repeating the same tests
   becomes less effective over time; tests need to be updated/varied
   (though repetition is fine, even useful, in automated regression
   testing).
6. **Testing is context-dependent** — no single universal approach;
   e.g. safety-critical software is tested differently than a
   simple internal tool.
7. **Absence-of-defects fallacy** — fixing every found defect doesn't
   guarantee success if the system still doesn't meet actual user
   needs. Verification alone isn't enough — validation matters too.

## Test Process (high level)

Test Planning → Test Analysis → Test Implementation → Test Completion,
with Monitoring & Control running throughout. The process is tailored
per context, not fixed.
