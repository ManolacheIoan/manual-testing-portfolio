# Scrum Sprint Concepts

Notes from Jira/Xray course (Section 3), continuing from Jira
fundamentals covered previously.

## Sprint

A fixed time period (commonly 1-2 weeks) during which the team works
on a set of pre-selected Stories. Short cycles force the team to
deliver small, testable pieces of work frequently, so problems surface
early rather than after months of undetected drift.

## Sprint Planning

The meeting at the start of a Sprint where the team looks at the
Backlog (already refined, with clear Acceptance Criteria) and decides
which Stories to commit to for that Sprint. The decision is based on
Story Points and the team's realistic capacity for that time period.

## Scrum Board & Workflow

- **Scrum Board**: visual representation of current Sprint work,
  organized into status columns (typically To Do → In Progress →
  Done, sometimes with an additional Review/Testing column).
- **Workflow**: the rule governing how an item (Story, Bug, Task)
  moves between those columns as work progresses.
- As a tester, the board is the source of truth for which Stories
  have reached a "ready to test" state — not something to wait to be
  told verbally.

## Velocity

The measure of how many Story Points a team completes per Sprint,
tracked across multiple Sprints. Used for future planning (e.g. "we
typically complete ~20 points per Sprint").

Distinct from Burndown/Burnup charts, which visualize progress within
a single Sprint:
- **Burndown chart**: how much work remains in the current Sprint
  (line trends down toward zero)
- **Burnup chart**: how much work has been completed so far in the
  current Sprint (line trends up)
- **Velocity**: the completed-points metric itself, tracked
  Sprint-over-Sprint — not a chart of a single Sprint's progress

## Sprint Retrospective

A meeting held at the end of each Sprint, focused on how the team
worked — not what was built (that's Sprint Review). Typical questions:
what went well, what blocked us, what do we change next Sprint. It's
team introspection, not task assignment and not a stakeholder
discussion about the product itself.
