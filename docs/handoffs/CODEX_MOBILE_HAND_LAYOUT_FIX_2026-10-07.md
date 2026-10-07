# Mobile hand-toggle layout fix — 2026-10-07

User approved moving the mobile hand toggle beside End Turn. This resolves the mobile Player Artifact tap overlap recorded in the earlier large regression review; that report describes the pre-fix version.

## Minimal change

In index.html, existing D5.2 mobile CSS positions `.d52-toggle` at the center of the turn-command row instead of above it. The mobile primary CTA host reserves 78px on its right for the existing button. The Attune action area reserves the same clearance when the primary CTA is absent. The toggle is 64×44px; minimum compact turn-row height changes from 42 to 44px to contain it.

The DOM button, click listener, manual/automatic tuck state, labels, ARIA expanded state and disabled behavior are preserved. The only JavaScript change is the existing mobile layout controller's minimum turn-row height. No gameplay or desktop rules changed.

## Verified

- 26/26 focused layout checks passed: 667×375, 844×390, 1024×667 and 1180×820; Attune, ACTION, open/tucked/open hand, Creature bounds, Artifact tap, rotation and page errors.
- Toggle remains within the turn row; at least 6px separates it from the phase CTA; primary CTA remains wider than the toggle.
- Actual touch interaction on the last Player Artifact opens its detail at all four sizes.
- Focused baseline/current hit tests at 844×390: 2/3/6/10 Artifacts, both owners. Baseline Player last tile was intercepted; current last tile centers resolve their own Artifact on both sides.
- Desktop 1440×900 geometry exactly matches the pre-layout version.
- Rotation waits for the viewport controller's settled DOM state, rather than assuming completion after a fixed 200ms delay. One visible toggle returns at every tested size.
- Re-ran Artifact syntax/status/FX tests and all four Echo Trials through UI without hints; all recorded checks passed, no pageerror.
- `git diff --check` passed.

Evidence directory:
`C:/Users/Warunyu.N/.codex/visualizations/2026/10/05/01a10a2c-621b-7ee0-894b-55863a750b1c/regression-20261007/`

Exact incremental diff: `mobile-hand-layout.patch`.
Checks: `hand-layout-results.json`, `hit-results.json`.
Screenshots: `hand-layout-667-open.png`, `hand-layout-844-open.png`, `hand-layout-1024-open.png`, `hand-layout-1180-open.png`, and corresponding tucked states.
Targeted Artifact/Trials results: `../artifact-ux-fix/results.json`.

No physical iPhone/Safari test and no deployment performed. The live Pages version still requires publication verification after deployment. No staging, commit or push performed; existing working-tree changes and untracked handoff/scratch files are preserved.
