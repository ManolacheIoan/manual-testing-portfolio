# Kanban, Bug Creation, and Xray Test Hierarchy

Notes from Jira/Xray course (Sections 4-5).

## Creating Bugs in Jira

When creating a bug/defect issue in Jira, typical fields completed
beyond Summary/Description (Steps to Reproduce, Actual vs Expected
Result):

- **Assignee** — who the bug is assigned to for fixing
- **Priority** — how urgent the fix is, from a business perspective
- **Severity** — how technically serious the bug is (functional impact)

Severity and Priority are tracked separately (see Module 1 notes) —
a bug can be Severity: Low but Priority: High, or vice versa,
depending on business context.

## Kanban Board

Kanban is an alternative to Scrum for organizing work — it does NOT
use Sprints or fixed time cycles. Work flows continuously through
status columns (commonly: To Do, In Progress, Done), with no
"planning" of a fixed batch of work every 2 weeks like in Scrum.

Kanban boards can still use Epics and Stories, same as Scrum — the
difference is purely in how time/work is organized (continuous flow
vs. fixed-length Sprints), not in the underlying issue types.

Common in teams handling ongoing/unpredictable work (e.g. support,
maintenance), where work arrives continuously rather than in
plannable batches.

## Xray Test Hierarchy

Xray adds several issue types on top of standard Jira issues, used
specifically for structured test management:

- **Test** — a single test case, defining the steps/conditions to
  verify. Can be executed multiple times via Test Execution.
- **Precondition** — a condition that must be true before running a
  test (e.g. "user must be logged in"). Can be linked to multiple
  tests.
- **Test Set** — a group of related Tests (e.g. "Login Tests").
  Groups Tests together for association with other Xray types.
- **Test Plan** — defines the scope of tests for a full test
  campaign/release, aggregating execution results across all
  included tests.
- **Test Execution** — a single instance of actually running a Test
  (or set of Tests), producing a result (Pass/Fail) for that run.
- **Sub Test Execution** — similar to Test Execution, but nested
  under a parent issue (e.g. a requirement).

**Hierarchy, largest to smallest** (parallels Epic to Story structure):

Test Plan (full campaign/release scope)
  -> Test Set (thematic group of tests)
    -> Test (individual test definition, the steps to follow)
      -> Test Execution (one run of those steps, with a Pass/Fail result)


## Test vs Test Execution

- **Test** = the definition, the steps that must be followed,
  reusable across many runs
- **Test Execution** = a single act of running those steps, producing
  one result (Pass/Fail) tied to that specific run

The same Test can have multiple Test Executions over time (e.g. run
today with Pass, run again after a code change next week with Fail).
The Test itself doesn't change, executions accumulate, each with its
own result and date.

## Test Case vs Test Scenario

- **Test Scenario**: a high-level description of what needs to be
  tested (e.g. "verify login functionality")
- **Test Case**: a concrete, specific test derived from a scenario
  (e.g. "login with valid credentials", "login with wrong password",
  "login with empty fields")

One Test Scenario typically produces multiple concrete Test Cases,
same relationship pattern as Epic to Story.
