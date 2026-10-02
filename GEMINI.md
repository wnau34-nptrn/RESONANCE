# WONDERBOUND: RESONANCE — STRICT AGENT SCOPE & REGRESSION LOCK

## PRIMARY RULE

FOLLOW THE USER'S REQUEST LITERALLY, NARROWLY, AND CONSERVATIVELY.

DO NOT EXPAND THE SCOPE.

DO NOT FIX, CHANGE, REDESIGN, REFACTOR, CLEAN UP, OPTIMIZE,
MODERNIZE, OR IMPROVE ANYTHING THAT THE USER DID NOT EXPLICITLY REQUEST.

If another issue is discovered:

REPORT IT.

DO NOT FIX IT.

"While I am here" changes are prohibited.

---

# 1. MINIMUM-DIFF POLICY

Always make the smallest safe source change required to satisfy the explicit request.

Before editing, ask:

"What is the minimum set of source lines required to solve this exact task?"

Use that set.

Do NOT:

- refactor surrounding code
- clean surrounding CSS
- merge unrelated selectors
- rename unrelated selectors
- rename unrelated functions
- rename unrelated variables
- reorganize files
- reorganize style blocks
- modernize architecture
- rewrite code for elegance
- remove legacy code unless explicitly requested
- run broad automatic formatting
- re-indent unrelated sections
- run Prettier or equivalent over large files
- change unrelated whitespace

A smaller safe patch is preferred over a cleaner-looking large patch.

---

# 2. INSPECT BEFORE EDITING

For every bug fix:

1. Inspect the current implementation.
2. Reproduce the issue when practical.
3. Identify the verified root cause.
4. Identify the exact code/CSS owner.
5. Inspect relevant parent/shared dependencies.
6. Only then edit.

DO NOT GUESS AND PATCH.

Do not add overrides before understanding the existing winning rule.

Do not assume the visually obvious selector is the actual owner.

---

# 3. ROOT-CAUSE OWNER RULE

Fix the narrowest existing owner responsible for the defect.

Prefer correcting the responsible rule over stacking another patch.

Do NOT use symptom-hiding techniques such as:

- random CSS overrides
- arbitrary transform
- arbitrary translateX / translateY
- negative margin hacks
- excessive overflow clipping
- font shrinking to hide layout pressure
- per-card hacks
- viewport hacks without verified cause

unless the user explicitly requests that technique.

If the true owner cannot be isolated safely:

STOP AND REPORT.

---

# 4. SCOPE DOES NOT TRANSFER

A component used as a reference is NOT permission to modify it.

Examples:

"Make Player match Enemy"

means:

MODIFY PLAYER ONLY.

DO NOT MODIFY ENEMY.

---

"Fix Mobile"

means:

DO NOT MODIFY DESKTOP.

---

"Fix landscape"

means:

DO NOT MODIFY portrait.

---

"Fix Hand expanded state"

does NOT mean:

redesign Hand.

---

"Fix one card"

does NOT mean:

modify other cards.

---

"Use Enemy as visual reference"

does NOT mean:

change Enemy styling or geometry.

---

# 5. SHARED SELECTOR SAFETY

Before modifying any shared selector, determine every relevant surface it affects.

Examples of potentially shared selectors:

- `.arena-row`
- `.card`
- `.board`
- `.battlefield`
- `.hand`
- generic responsive selectors
- shared state selectors

If the user requested Player-only behavior:

DO NOT modify a selector that also changes Enemy unless you can prove Enemy remains unchanged.

If the user requested Mobile-only behavior:

DO NOT modify a rule that changes Desktop.

If the user requested one state:

DO NOT alter other states unless necessary and verified.

If a shared selector affects anything outside the requested scope:

USE A NARROWER EXISTING SELECTOR.

If that is not possible:

STOP AND REPORT.

Do NOT silently broaden scope.

---

# 6. REGRESSION SAFETY — ABSOLUTE

Every change must preserve unrelated existing behavior.

A fix is NOT complete if it solves the requested issue but breaks another area.

Before finalizing any change:

1. Identify the exact area intentionally changed.
2. Identify nearby/shared components that could be affected.
3. Verify those unrelated areas remain unchanged.
4. Run the narrowest relevant regression checks.
5. Compare before vs after where practical.
6. If unrelated behavior changes, treat the task as FAILED.

Do not accept:

"the requested bug is fixed"

if another component, screen, breakpoint, state, or gameplay behavior regresses.

---

# 7. NO COLLATERAL DAMAGE

The requested change must NOT cause collateral changes to:

- other UI components
- Enemy side
- Desktop
- Portrait mode
- Hand
- Card Detail
- Mulligan
- Graveyard
- Battlefield layout
- Keeper HUD
- Landmark HUD
- typography
- artwork framing
- animation
- interaction behavior
- gameplay
- card data
- responsive breakpoints outside scope

unless explicitly requested.

If the patch affects a shared selector, function, layout owner, or state:

verify every relevant dependent surface before accepting the patch.

If safe isolation cannot be proven:

STOP AND REPORT.

DO NOT APPLY A BROADER PATCH.

---

# 8. BEFORE / AFTER REGRESSION CHECK

For UI changes, compare BEFORE vs AFTER for:

- the explicitly changed component
- adjacent components
- shared selector users
- relevant interaction states
- relevant responsive states

Only the requested component should materially change.

If unrelated elements:

- move
- resize
- disappear
- restyle
- clip
- overflow
- change alignment
- change behavior

because of the patch:

THE PATCH FAILS REGRESSION.

---

# 9. RESPONSIVE UI REGRESSION RULE

For responsive UI changes, verify at minimum when relevant:

- requested viewport
- same component in alternate state
- Player equivalent
- Enemy equivalent
- collapsed state
- expanded state
- Desktop if shared CSS may apply
- Card Detail if card styles are shared

Do not claim PASS from a single screenshot.

Do not claim responsive safety from one viewport only when the rule affects multiple responsive sizes.

---

# 10. PASS CONDITION

A task passes only when BOTH are true:

1. The explicitly requested issue is fixed.
2. Unrelated behavior remains unchanged.

Fixing the requested bug while creating a new regression is a FAIL.

---

# 11. LOCKED SYSTEMS

Unless the user explicitly asks, DO NOT modify:

- Gameplay
- Turn Flow
- Phase Flow
- Combat
- Damage
- Targeting
- Resonance
- Refill
- Attune
- Journey
- Restore
- Landmark rules
- Keeper rules
- AI
- card data
- Cost
- Requirement
- AT
- HP
- abilities
- triggers
- tokens
- deck rules
- draw logic
- Grave
- win / lose conditions
- progression
- rewards
- artwork
- artFocus
- object-position
- artwork source ratio
- artwork generation data

Do not silently change locked behavior.

---

# 12. CORE LOCK POLICY

Any file or document marked:

- CORE LOCK
- FINAL LOCK
- LOCKED
- CANONICAL
- SOURCE OF TRUTH

must be treated as authoritative.

Do not modify behavior governed by a Lock unless the user explicitly requests an unlock/change.

If current implementation conflicts with a Lock:

REPORT THE CONFLICT.

Do not silently reinterpret or rewrite the Lock.

---

# 13. PRESENTATION-FIX RULE

For presentation-only defects:

Prefer CSS/layout fixes.

Do not modify JavaScript unless JavaScript is verified to be the root cause.

If JavaScript modification appears necessary but was not explicitly authorized:

STOP AND REPORT BEFORE EDITING.

Do not change DOM structure unless explicitly required.

Do not modify rendering logic for a CSS-only defect.

---

# 14. CSS SAFETY

For CSS tasks:

Inspect when possible:

- computed styles
- selector specificity
- cascade order
- parent geometry
- width / height
- min/max dimensions
- aspect-ratio
- flex behavior
- grid behavior
- inherited values
- percentage sizing
- overflow
- responsive media queries
- state-specific rules
- `!important`

Do not assume a selector is safe because its name looks correct.

Verify what it actually matches.

---

# 15. GEOMETRY SAFETY

When preserving an aspect ratio:

do not independently clamp only width or only height if that changes the intended ratio.

If available space becomes constrained:

scale both dimensions proportionally unless the explicit design says otherwise.

Do not solve geometry defects by:

- clipping content
- hiding stats
- hiding text
- shrinking essential typography
- distorting artwork
- stretching the card

---

# 16. RESPONSIVE SAFETY

Mobile request ≠ permission to modify Desktop.

Landscape request ≠ permission to modify Portrait.

Player request ≠ permission to modify Enemy.

Hand issue ≠ permission to redesign Battlefield.

Battlefield issue ≠ permission to redesign Hand.

One breakpoint request ≠ permission to rewrite all breakpoints.

Use the narrowest responsive scope possible.

---

# 17. ARTWORK SAFETY

Unless explicitly requested, DO NOT modify:

- artwork files
- image sources
- base64 images
- artFocus
- object-position
- object-fit strategy
- focal presets
- artwork metadata
- image crop logic
- artwork generation prompts

If container geometry is wrong:

fix the container.

Do not compensate by editing artwork.

---

# 18. TYPOGRAPHY SAFETY

Do not reduce essential text size merely to make layout fit.

Preserve readability.

Do not create per-card font-size hacks.

Do not hide required information.

Solve geometry through layout before sacrificing typography.

---

# 19. FILE-SCOPE RULE

If the user specifies allowed files:

ONLY MODIFY THOSE FILES.

If another file is required:

STOP.

Report:

- required file
- why it is required
- why current allowed file is insufficient
- proposed minimal change

Wait for approval.

Never silently expand file scope.

---

# 20. JAVASCRIPT GUARD

For UI/presentation fixes:

JavaScript should remain unchanged unless proven necessary.

If JavaScript is not explicitly authorized:

DO NOT MODIFY IT.

If JavaScript appears to be the real cause:

STOP AND REPORT.

Do not alter:

- event timing
- gameplay state
- action state
- animation sequencing
- game logic

for a presentation-only defect.

---

# 21. NO AUTONOMOUS PRODUCT DECISIONS

Do not make new design/product decisions unless explicitly requested.

Do not decide on your own that:

- another layout is better
- another UX is better
- another architecture is cleaner
- another card balance is better
- another visual style is more modern
- another mechanic is easier

Implementation tasks are not permission to redesign.

Suggestions may be reported separately only when requested.

---

# 22. DISCOVERED ISSUES

If you discover an unrelated issue:

DO NOT FIX IT.

Use:

DISCOVERED — OUTSIDE CURRENT SCOPE:
[brief description]

Then continue only with the requested task.

Do not convert discovered issues into extra implementation work.

---

# 23. UNCERTAINTY RULE

If you are not confident that a proposed change stays inside scope:

DO NOT GUESS.

STOP AND REPORT.

Explain:

- what is uncertain
- what dependency exists
- what additional scope would be required

It is better to stop than to cause collateral damage.

---

# 24. GIT SAFETY

Do NOT:

- stage
- create branch
- commit
- push
- create Pull Request
- merge
- deploy
- modify GitHub settings
- modify CI/CD
- modify Netlify settings

unless the user explicitly requests that exact step.

Local implementation approval does NOT imply GitHub approval.

Testing approval does NOT imply commit approval.

Commit approval does NOT imply merge approval.

PR approval does NOT imply deployment approval.

---

# 25. REVIEW GATE

When the user asks for review before Git actions:

after local implementation and validation:

1. Report verified root cause.
2. Report exact changed files.
3. Report exact source changes.
4. Show relevant git diff.
5. Show validation results.
6. Show regression results.
7. Show git status.
8. STOP.

Do not proceed to Git actions until explicitly approved.

---

# 26. PATCH IMMUTABILITY AFTER REVIEW

If a patch has been reviewed and approved:

do NOT change it before commit/PR.

Do not:

- improve it
- optimize it
- reformat it
- rename selectors
- add unrelated comments
- adjust another breakpoint
- fix another bug

If source changes after approval:

the patch requires a NEW review.

---

# 27. DO NOT AUTO-CLEAN THE PROJECT

Do not use a bug fix as an opportunity to:

- consolidate CSS architecture
- remove legacy blocks
- remove duplicate selectors
- remove `!important`
- rewrite media queries
- convert Flex to Grid
- convert Grid to Flex
- move inline code into new files
- split files
- merge files
- reorganize folders

unless explicitly requested.

Messy code is NOT permission to refactor.

---

# 28. TEST WHAT YOU CHANGED

Validation must match the task.

For a UI change, test the actual rendered UI when browser/runtime access is available.

Do not rely only on static source inspection if runtime evidence is available.

For visual geometry changes, prefer evidence such as:

- rendered width
- rendered height
- aspect ratio
- computed style
- bounding rectangle
- screenshot
- state transition test

Do not claim PASS without evidence appropriate to the task.

---

# 29. SHARED-OWNER REGRESSION RULE

If code being modified is shared by multiple surfaces:

list the major affected surfaces before editing.

Example:

A shared `.arena-row .card.board` rule may affect:

- Player
- Enemy
- READY
- EXHAUSTED
- selected
- target
- multiple board counts
- multiple mobile sizes

If the user requested only Player:

either:

A. use a Player-specific selector

or

B. prove every other matched surface remains unchanged.

If neither is possible:

STOP AND REPORT.

---

# 30. FINAL AGENT CHECK BEFORE EVERY EDIT

Before modifying source, verify:

1. Did the user explicitly request this change?
2. Is this exact code responsible for the requested behavior?
3. Is this the narrowest safe owner?
4. Will this affect anything outside scope?
5. Is the selector/function shared?
6. Am I changing a locked behavior?
7. Can the same result be achieved with a smaller patch?
8. Have I verified the root cause instead of guessing?
9. What regression could this change cause?
10. How will I prove unrelated behavior remains unchanged?

If #1 or #2 is NO:

DO NOT EDIT.

If #4 or #6 is YES and not explicitly authorized:

STOP AND REPORT.

If a smaller safe patch exists:

USE THE SMALLER PATCH.

---

# 31. COMPLETION DEFINITION

A task is complete only when:

- the explicitly requested issue is addressed
- the root cause is verified
- required tests pass
- relevant regression tests pass
- unrelated behavior remains unchanged
- scope is respected
- no unauthorized files were modified
- no unauthorized Git actions occurred

A task is NOT more complete because extra things were improved.

---

# GOLDEN RULE

DO EXACTLY WHAT WAS ASKED.

NO MORE.

NO LESS.

FIX THE REQUESTED ISSUE WITHOUT BREAKING ANYTHING ELSE.

NO COLLATERAL DAMAGE.

IF A CHANGE FIXES ONE AREA BUT BREAKS ANOTHER:

THE TASK FAILS.

IF YOU DISCOVER ANOTHER ISSUE:

REPORT IT.

DO NOT FIX IT.

IF YOU ARE NOT SURE:

STOP AND REPORT.

DO NOT "HELP" BY MAKING EXTRA CHANGES.