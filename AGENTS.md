# WONDERBOUND: RESONANCE — CODEX AGENT RULES

## Highest Priority

Follow the user's request literally and narrowly.

Do not expand scope.

Do not fix, redesign, refactor, clean up, optimize, or improve anything
that was not explicitly requested.

If another issue is discovered:
REPORT IT.
DO NOT FIX IT.

## Minimum Diff

Always make the smallest safe patch required by the task.

No "while I am here" changes.
No unrelated formatting.
No unrelated cleanup.
No opportunistic refactoring.

## Inspect Before Edit

For bug fixes:

1. Inspect current implementation.
2. Reproduce when practical.
3. Identify verified root cause.
4. Identify the narrowest responsible owner.
5. Only then edit.

Do not guess and patch.

## Scope Does Not Transfer

"Make Player match Enemy"
means modify Player only.

"Fix Mobile"
does not authorize Desktop changes.

"Use X as reference"
does not authorize modification of X.

## Shared Selector / Shared Owner Safety

Before changing shared CSS, functions, state, or components,
identify what else they affect.

If the requested scope is Player-only:
do not modify a shared rule that changes Enemy.

If safe isolation cannot be proven:
STOP AND REPORT.

## Regression Safety

A fix is successful only when:

1. the requested issue is fixed, and
2. unrelated behavior remains unchanged.

If one area is fixed but another area breaks:
THE TASK FAILS.

Verify relevant adjacent/shared surfaces before declaring PASS.

## Locked Systems

Unless explicitly requested, do not modify:

- gameplay
- turn flow
- combat
- Resonance
- Journey / Landmark
- AI
- card data
- Cost / Requirement
- AT / HP
- abilities
- artwork / artFocus
- unrelated responsive contexts

CORE LOCK / FINAL LOCK / CANONICAL documents are authoritative.

## Presentation Fixes

Prefer CSS/layout fixes for presentation defects.

Do not modify JavaScript unless it is verified as the root cause.

If JavaScript or another file is required beyond the user's allowed scope:
STOP AND REPORT FIRST.

## Git Safety

Do not stage, branch, commit, push, create PR, merge, or deploy
unless explicitly instructed for that exact step.

## Review Gate

When the user requests review before Git actions:

- report root cause
- show exact diff
- show validation
- show regression results
- show git status
- STOP

## Golden Rule

DO EXACTLY WHAT WAS ASKED.

NO MORE.
NO LESS.

FIX THE REQUESTED ISSUE WITHOUT BREAKING ANYTHING ELSE.

IF IN DOUBT:
STOP AND REPORT.