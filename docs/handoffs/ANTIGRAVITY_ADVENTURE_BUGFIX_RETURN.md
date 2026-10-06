# Antigravity → Codex: Adventure bug-fix RETURN

Date: 2026-10-06 · Branch `codex/adventure-assets` · HEAD `d7be81e8988b4145cdb3881775af17f6159159ed`

Nothing was staged, committed, pushed, merged, PR'd or deployed. Working-tree changes only.

## Baseline received
- `index.html` SHA-256 before my edits: `20090de9912855bc4b48cffed6b0f86b3e815c53e9b72aefb7efd7bc2add2700` (matches handoff).
- `validation-report.json` SHA-256: `b58c0f13…31436d` — unchanged after my work (verified).
- Snapshot of received `index.html` kept outside the repo (Antigravity scratch dir, `index.baseline.html`); delta computed against it.
- `index.html` after my edits: `c5173376fcdd7b6ce950aa28a8fa8addd0c36dd49aecebcb3130b7a80bee13f5`.

## Root cause & owner
**P1** — `beginHandPlay` override (p23 section, ~line 38055): after `game.p3dQueueChoice(...)` set `pendingChoice`, nothing re-rendered, so `[data-p3d-choice-layer]` never drew. Owner: that override only.
**P2** — Adventure `load()` (~line 40049) accepted any `{version:1, completed:{…}}` object without defaulting `mastery`/`achievements`/`owned`/`echoes`, so UI code read `undefined.p1`.

## Exact changes (delta = 2 hunks, +4/−2 lines, `index.html` only)
See `ANTIGRAVITY_ADVENTURE_BUGFIX_DELTA.patch` (reverse-applies cleanly against the working tree).
1. `beginHandPlay`: store queue result in `p23Queued`, `if(p23Queued)render();`, `return p23Queued;` (return value, options, targetOwner, sourceUid, Cost flow unchanged).
2. `load()`: reject non-object/array `completed` (fallback null as before); fill missing/invalid `mastery`, `achievements`, `owned`, `echoes` from `initial()`; drop invalid `puzzles` / non-`true` `tutorialCompleted`; keep valid values. Storage key/version unchanged; no reward/unlock changes.

## Results (headless Chrome via CDP, isolated temp profile; audio `file://` fetch errors filtered — environmental)
Evidence logs: `docs/handoffs/evidence-antigravity/`.

### P1
| Check | Result |
|---|---|
| Baseline reproduces (et2 Omen: pendingChoice set, no layer) | PASS (reproduced) |
| et2 desktop: layer shows right after play, payment opens after pick, nothing paid before confirm | PASS |
| et2 desktop: confirm → paid once (committed fracture 3), Omen + Fractureling in grave, winner=0 via normal UI, no hint | PASS |
| et2 cancel payment: no resources lost, card kept, no stale pendingChoice | PASS (desktop, mobile) |
| et2 restart with choice open: pendingChoice cleared | PASS (desktop, mobile) |
| et3: layer shows, options include enemy; enemy Rootkeeper returned; paid once | PASS (desktop, mobile) |
| et3 full win (post-RETURN attack on Keeper) | NOT TESTED |
| Break the Vessel: layer shows, 2 options (hand injected by script — setup only, not win evidence) | PASS (desktop, mobile) |
| Mobile (844×390 touch emulation): et2 full flow incl. win, et3, Break | PASS |
| et1 Equipment/RIFTSTRIKE win, et4 Combat/Journey/Claim win | NOT TESTED |
| Drag-to-play entry point | NOT TESTED |

### P2 (baseline vs current)
| Case | Baseline | Current |
|---|---|---|
| no save / malformed JSON / version 2 | safe fallback | safe fallback (PASS) |
| `{version:1,completed:{}}` → Basic | **pageerror `reading 'p1'`** | Basic 10 nodes (4 puzzles), Story 14, Expedition disabled, no errors (PASS) |
| nulls/arrays/strings in fields | pageerror | normalized, `completed` kept, no errors (PASS) |
| `completed` is an array | unusable | safe fallback to initial (PASS) |
| valid full v1 save | preserved | preserved byte-for-byte (PASS) |
| partial (completed + puzzles only) | pageerror | completed/puzzles kept, others defaulted (PASS) |
| p1 first-win reward once / p2 unlock / reload / replay no re-reward | — | NOT TESTED (needs full battle win) |
| Guide open/close, spotlight, walkthrough, portrait gate | — | NOT TESTED (my guide-open probe was inconclusive; same result on baseline) |

### Other regressions
- Inline scripts syntax: 47 scripts, 0 failures — PASS. `git diff --check` clean — PASS.
- Stage/card/reward definitions: delta touches only the two hunks above, so definitions are unchanged by construction; no separate before/after dump run — NOT TESTED as a dump.
- Lore Next/Back/Skip, Normal Duel (mulligan/Attune/AI), Deck Builder, et2/et3 hint levels, Story branch battle entry/exit: NOT TESTED.
- iOS/Safari, all bosses: NOT TESTED.

## Reproduce
- P1: Adventure → Basic → et2 → tap Omen of Collapse → play. Expect choice dialog immediately.
- P2: `localStorage.setItem('wonderbound_adventure_v1', JSON.stringify({version:1,completed:{}}))`, reload, Adventure → Basic.

## Limitations / blocker status
Several regression items above are NOT TESTED, so per handoff rules this is **not declared complete**; P1/P2 targeted behaviour passes. Codex should re-test remaining items.

## Discovered — outside scope (not fixed)
- `nulls` case: numeric string `echoes:'9'` is reset to 0 rather than coerced (intentional, conservative).

## git status
```
 M assets/art/adventure/previews/validation-report.json   (Codex, untouched by me)
 M index.html
?? docs/handoffs/   (HANDOFF.md, RETURN.md, DELTA.patch, evidence-antigravity/)
```
