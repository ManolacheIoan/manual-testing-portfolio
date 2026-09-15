# Jira Fundamentals — Core Concepts

Notes from Jira/Xray course sections, covering the building blocks of
how work is organized and tracked in Jira.

## Core Item Types

- **Epic** — a large body of work, too big to complete in one sprint;
  groups related Stories together (e.g. "Implement Login Module")
- **Story** — a single user-facing piece of functionality, written in
  standard format: *"As a [role], I should be able to [action], so
  that [benefit]"*. Example: "As a client I should be able to enter
  my email and password in the login page, so that I can login."
- **SubTask** — a smaller piece of work that breaks down a Story into
  more manageable chunks (e.g. "Create email field" / "Add password
  validation")
- **Component** — a sub-section of a project, used to group issues
  into smaller logical parts (e.g. "Team 1", "Backend", "UI")
- **Release** — a version/milestone that groups completed work meant
  to ship together (e.g. "Login release 01/26")

## Acceptance Criteria

The specific, testable conditions that define when a Story is
considered "done." Written during backlog refinement, based on
discussion of edge cases. Example, for a login Story:
- Create two edit boxes (email, password)
- Show error messages when invalid information is entered
- Special characters are not allowed

Acceptance Criteria are the direct input for deriving test cases
(same logic as Equivalence Partitioning / Boundary Value Analysis —
each criterion becomes something to verify).

## Story Points

A **relative** measure of a Story's complexity/size — not exact hours.
Commonly estimated using a Fibonacci-like scale (1, 2, 3, 5, 8, 13).
The team compares Stories to each other ("this feels twice as complex
as that 3-point Story, so it's a 5") rather than estimating precise
time.

## Backlog Refinement (Grooming)

A recurring team meeting (commonly weekly) where vague Backlog items
are turned into clear, workable Stories before they enter a Sprint.
During refinement, the team:
1. Discusses the Story and asks clarifying questions (e.g. "what
   happens with an empty email field?")
2. Defines/refines Acceptance Criteria based on that discussion
3. Breaks large Stories into SubTasks if needed
4. Estimates the Story with Story Points

Goal: nobody starts a Sprint with ambiguous, unworkable Stories.

## Board / Backlog / Status Workflow

- **Backlog** — the full list of Stories not yet started/planned
- **Board** — visual view of work in progress, organized by status
  columns (To Do → In Progress → Done)
- Every issue moves through this workflow as work progresses

## Note on tooling

Jira can run self-hosted/local (e.g. `localhost:8080` in course demos)
or as a cloud-hosted product (Atlassian-managed). The underlying
concepts (Epics, Stories, Acceptance Criteria, Story Points, Backlog
Refinement) are identical regardless of hosting — infrastructure setup
is not a tester's concern, only how to use the tool.
