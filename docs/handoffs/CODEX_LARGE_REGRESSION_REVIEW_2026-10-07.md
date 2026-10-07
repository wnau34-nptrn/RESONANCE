# Large regression review — 2026-10-07

## Decision: HOLD

Review requested before Dev/Main. No game source edits, Git staging, commits, pushes, merges or deployments were performed in this review. One confirmed pre-existing mobile usability defect remains. The live Pages deployment is also behind Main, as verified earlier in this session.

## Reviewed version and exact diff

- Main/HEAD baseline: `4a94b290848e2a25a08ae67c9efb2394f7c69eca`.
- Current index.html SHA-256: `6e5c27d68b38a6eefdf44994ad15c9654400f76d70606da5c329693728233254`.
- Current diff: index.html, 323 added / 3 removed lines. Artifact presentation definitions, permanent markup, detail status, Artifact event presentation, and scoped CSS. No Adventure source delta in this working tree.
- Exact full diff: `C:/Users/Warunyu.N/.codex/visualizations/2026/10/05/01a10a2c-621b-7ee0-894b-55863a750b1c/regression-20261007/reviewed-working-tree.patch`.
- Git status snapshot: same evidence directory, `git-status.txt`.

## Confirmed findings

### P2 — Mobile hand toggle intercepts taps on Player's last Artifact

Reproduction: Chrome mobile/touch emulation, 844×390; enter a Duel, populate Player's Artifact rail with two or more Artifacts, scroll to the bottom if necessary, then tap the center of the last Artifact while the hand is expanded. The tap hits `.d52-toggle` rather than the Artifact. A real Playwright click on the last tile timed out with `d52-toggle intercepts pointer events`; other Artifact details opened normally. The Enemy rail did not have this interception.

This is present in both baseline Main and current working tree. Tested counts: 2, 3, 6 and 10, both owners. Current tiles are taller (34px vs baseline 25px), but this does not introduce the existing interception.

Verified owner: mobile hand-toggle absolute placement in index.html near line 35711 overlaps the Player Artifact rail. Toggle z-index is 91; Artifact rail z-index is 5 (near line 24329). In current 844×390 layout the last Player tile occupies x=770,y=161,width=66,height=34; its center is under the hand toggle. `document.elementFromPoint` resolves the toggle. Corresponding Enemy tile center resolves its Artifact.

Suggested next patch, requiring a separate fix request: reserve an unobstructed area for the hand toggle or reserve clearance in the mobile Player Artifact rail. Verify both hand states, Artifact counts, scroll reachability and both owners. Do not change combat, Enemy placement, or desktop to solve this mobile Player interaction.

Evidence: `hit-results.json`, `hit-baseline-2.png`, `hit-current-2.png`, `hit-current-3.png`, `blocked-0-canopy.png`. All in the evidence directory below. Fixture population is explicitly isolated; this is a layout/tap test, not a claim of obtaining ten Artifacts during a real match.

### Deployment prerequisite — live URL serves older Adventure

Earlier read-only verification in this session found Main and Dev on `4a94b29`, while Pages' last successful run deployed `cba848f85e21164cbc281ec8489a6410cfeeb39e`. The actual game URL returned the old `adv-chapter`/`adv-nodes` map and no `atlasMode`. This explains the installed icon showing the old Adventure independently of mobile cache.

URL: https://wnau34-nptrn.github.io/RESONANCE/
Run: https://github.com/wnau34-nptrn/RESONANCE/actions/runs/37268488643

Deployment must be handled and re-verified separately after approval; this review did not trigger it.

## Validation and regression evidence

Evidence root:
`C:/Users/Warunyu.N/.codex/visualizations/2026/10/05/01a10a2c-621b-7ee0-894b-55863a750b1c/regression-20261007/`

- Broad suite: `results.json`, 58/58 checks passed. Corresponding script is `../regression-20261007.cjs`.
- Engine/UI suite: `engine-results.json`, 26/27 checks passed; the failure is Player's final Artifact tap, described above. Corresponding script is `../regression-engine-20261007.cjs`.
- Focused baseline/current hit-test and Lore suite: `hit-results.json`; script `../regression-hit-20261007.cjs`.
- Targeted Artifact/Trials suite re-run this session: `../artifact-ux-fix/results.json`, all recorded checks passed; script `../artifact-ux-fix/verify.cjs`.

Passing checks:

1. All 47 inline scripts parsed, and `git diff --check` passed.
2. Compared runtime Game prototype function/getter definitions, complete card data, Landmark data, all Starter definitions, and Adventure stage definitions against Main: all identical.
3. Deterministic engine fixtures: eight actual curated Starter profiles × three seeds = 24 completed Duels, no blocked choices, rounds 5–17. Full final snapshots and results matched Main exactly. Human auto-policy and AI stepping are test drivers; these are not 24 UI playthroughs or balance certification.
4. Actual Normal Duel UI: Mulligan selection, confirm, Attune, End Turn, AI resolution and return to Player Turn.
5. Four Echo Trials won through mobile UI without hints. Equipment/payment, Omen/sacrifice/choice, Return/enemy targeting and Combat/Journey/Claim exercised.
6. Artifact summary/status bounds at 667×375, 844×390, 1024×667 and 1440×900, both owners. Rails with 0/1/3/6 Artifacts are scroll containers; overflow alone is not a clipping failure. A separate tap test identified the overlap above.
7. Adjacent Creature, Keeper and hand geometry matched Main in all four viewports. Mobile hand toggle preserved Creature bounds on both sides.
8. Every limited Artifact's used/reset state checked for both owners; Idol/Nursery dormant state checked on opponent turns. Real engine final cap keys for Canopy/Edge checked by event emission.
9. New Game repeated event IDs preserve Artifact FX; same-game replay deduplicates. Citadel real BUFF identifies the correct recipient once without inventing an absent source UID. Reduced motion suppresses the new beam.
10. All ten Artifact detail types opened for Enemy. Nine of ten opened for Player in a ten-Artifact fixture; the final one encountered the verified toggle overlap.
11. Adventure Basic has 10 nodes; fresh progress unlocks p1 and four puzzles. Story has 14 nodes and fresh progress correctly locks them. Expedition remains disabled.
12. Tutorial navigated all 17 pages with Back/Finish and returned to map, on mobile and desktop. Story Lore Next changes dialogue, Back restores the earlier line, Skip selects the last line.
13. Entered and confirmed return to map from all 14 Story stages on mobile using a clearly labeled fully-unlocked progress fixture; this is not proof of beating all Story bosses. Basic enter/return checked mobile and desktop.
14. Malformed JSON, partial progress and invalid optional save-field types loaded without page errors and retained correct stage unlocks.
15. Mobile→desktop→portrait→mobile viewport ownership transitions checked. Portrait lock screenshot captured. No pageerror in completed suites.

## Limits

No physical iPhone/Safari installed-app test, no physical Android standalone test, no exhaustive combination of every ability/card pair, no full UI victory in every Story stage, and no new balance/reward redesign. Deployment was not performed. Console/network requests were not used as an exhaustive asset inventory check; no claim of universal asset/network cleanliness.

The earlier passing targeted Artifact report remains valid within its stated coverage. This broader review adds a pre-existing blocker that the earlier narrower check did not cover.

## Git status at review

Modified: `index.html`.

Pre-existing untracked paths preserved: Antigravity Artifact handoff/delta/return documents, Codex Artifact review/fix-return documents, `docs/handoffs/evidence-artifact-ux/`, and `scratch/`. This review adds this report only inside the repository; test harnesses, screenshots, raw results and diff snapshot are outside the repository in the permitted evidence directory.

Do not stage `scratch/` or all untracked files blindly. No release PASS is declared until the mobile tap overlap is resolved or explicitly accepted, followed by scoped retesting and publication verification.
