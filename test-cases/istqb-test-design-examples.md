# ISTQB Test Design Technique Examples

Practical applications of formal test design techniques, worked through
during QA training.

## 1. Equivalence Partitioning + Boundary Value Analysis

**Field under test:** Password length, accepted range 8–20 characters.

| Length | Expected Result | Zone |
|---|---|---|
| 7 | Invalid | Lower boundary − 1 |
| 8 | Valid | Lower boundary (exact) |
| 9 | Valid | Lower boundary + 1 |
| 14 | Valid | Mid-range (equivalence class representative) |
| 19 | Valid | Upper boundary − 1 |
| 20 | Valid | Upper boundary (exact) |
| 21 | Invalid | Upper boundary + 1 |

**Why exact boundaries matter:** a validation bug written as
`length < 8 || length >= 20` (using `>=` instead of `>`) is only caught
by the test at exactly 20 characters — all other values, including 19
and 21, pass regardless of the bug.

## 2. Decision Table Testing

**Business rule:** Video playback access requires an active subscription
AND a non-suspended account.

With 2 binary conditions → 2² = 4 mandatory rules.

| Condition | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
|---|---|---|---|---|
| Active subscription? | Yes | Yes | No | No |
| Account suspended? | No | Yes | No | Yes |
| **Access granted?** | YES | NO | NO | NO |

**Note:** Rules 2–4 all deny access, but for different reasons —
a well-designed system should surface a distinct, specific error
message per rule, not one generic "Access denied" for all three.

## 3. State Transition Testing

**System:** User account with 3 states — Active, Suspended, Deleted
(Deleted is final/irreversible).

**Valid transitions (5):**
1. Active → Suspended (admin suspends)
2. Active → Deleted (user deletes account)
3. Suspended → Active (admin lifts suspension)
4. Suspended → Deleted (admin permanent deletion)
5. Deleted → (no outgoing transitions — terminal state)

**Invalid transitions to test explicitly (2):**
1. Deleted → Active (must be blocked)
2. Deleted → Suspended (must be blocked)

**Rule:** every outgoing transition from a terminal state must be
tested individually — blocking one path does not guarantee the other
is blocked too.
