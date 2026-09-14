# ISTQB Foundation Level — Chapter 1: Test Activities, Testware & Process Context

Continuation of Chapter 1 notes — detailed breakdown of the test
process activities, using the course's own worked example (an online
course platform: student registration, enrollment, quizzes).

## The Six Test Activities, with the course's worked example

| Activity | What it means | Example (course platform) |
|---|---|---|
| Test Planning | Define objectives, choose approach within constraints | Team decides to test registration, course creation, video lessons, quizzes; writes a test plan, assigns tasks, sets schedule |
| Monitoring & Control | Ongoing check of progress vs. plan; take corrective action | Video lesson tests fall behind — team reassigns a tester and extends the schedule by 2 days |
| Test Analysis | Analyze test basis, identify testable conditions ("what to test?") | From "students can't enroll without completing prerequisites" → derive the test condition: enrollment must be blocked without prerequisites |
| Test Design | Turn conditions into concrete test cases ("how to test?") | Test case: log in as student, try to enroll without meeting prerequisites, expect an error message |
| Test Implementation | Build test environment, organize test cases into suites | Set up test accounts, upload test courses, group cases into suites like "Instructor Features" / "Student Features" |
| Test Execution | Run the tests, compare actual vs expected, log results | Tester tries to enroll without prerequisites — system correctly shows an error — test marked as passed |
| Test Completion | Wrap up: report, archive testware, document lessons learned | Tests done, results summarized in a report, test data cleaned, lessons learned documented |

## Key distinction: Test Analysis vs Test Design

- **Test Analysis answers "what to test?"** — identifying testable
  conditions from the test basis (requirements, user stories)
- **Test Design answers "how to test?"** — turning those conditions
  into actual test cases, with concrete inputs and expected results

This is a subtle but important distinction — analysis defines the
*coverage target*, design defines the *concrete steps* to hit it.

## Testware — output work products per activity

| Activity | Typical Work Products |
|---|---|
| Test Planning | Test plan, test schedule, risk register, entry/exit criteria |
| Monitoring & Control | Test progress reports, control directives, risk info |
| Test Analysis | Prioritized test conditions, defect reports (on the test basis itself) |
| Test Design | Prioritized test cases, test charters, coverage items, test data/environment requirements |
| Test Implementation | Test procedures, manual/automated scripts, test suites, test environment items (stubs, drivers, simulators, service virtualization) |
| Test Execution | Test logs, defect reports |
| Test Completion | Test completion report, improvement action items |

## Test Process in Context

Testing is never done in isolation — it's shaped by contextual
factors that affect strategy, automation level, coverage, and
reporting:

- **Stakeholders** — needs, expectations, willingness to cooperate
- **Team members** — skills, experience, availability, training needs
- **Business domain** — criticality, risk, market needs, legal/regulatory requirements
- **Technical factors** — software type, architecture, technology used
- **Project constraints** — scope, time, budget, resources
- **Organizational factors** — structure, existing policies and practices
- **SDLC** — engineering practices, development methods in use
- **Tools** — availability, usability, compliance

Takeaway: the *same* test process activities apply everywhere, but
*how* they're carried out (how much automation, how detailed the
testware, how strict the reporting) depends entirely on this context —
consistent with Testing Principle #6 (testing is context-dependent).
