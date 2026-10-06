# Adventure assets: review existing files before generation

User instruction, 2026-10-06: create each asset once, inspect the result first, and prevent duplicate generation across agents.

## Current gate

**STOP GENERATION.** No new imagegen requests, image edits, retries or variants in this review round. Inventory and inspect files already present. A failed image remains a candidate with specific defects; further correction requires explicit user approval for that asset.

The previous README, manifest and validation describe delivery 01 and are stale for the new raster files. A `blocked` or missing manifest entry is not evidence that an image needs generation. Reconcile actual files before changing status. File existence is not a visual PASS.

## Existing outputs to reuse and inspect

`previews/generation-log.json` records 14 primary assets with existing source/export pairs:

- Atlas: `maps/living-atlas-v2-source.png` and `maps/living-atlas-v2.webp`. Retain the earlier style proof as history; do not generate another map.
- Eight characters in `characters/`: liora, aurel-veyr, nym-avar, varkesh-thane, orun-kael, fractured-host, seris-vale and eira-mossborn. Each has a `-source.png` and a delivery `.png`.
- Three modes in `modes/`: basic, story and expedition, with `-source.png` and `.webp` pairs.
- Two scenes in `scenes/`: act1-opening and act1-ending, with `-source.png` and `.webp` pairs.
- Existing 21 SVGs and 24 stage thumbnails from delivery 01 remain available. Preserve them.

The source/export pairs are one artwork each, not separate generation tasks. Eight character icons should be derived from inspected existing character sources. Do not generate portraits again for icons. Do not claim icons exist until their actual files have been checked.

## Required sequence for any later authorized generation

1. Check the asset ID against actual files, manifest, generation log and pending requests. Reuse existing results; wait for in-flight requests. Never issue a duplicate request because an old manifest says blocked.
2. Record the asset ID, attempt, exact prompt, references and pending status before requesting one image. Do not generate variants or run multiple assets before reviewing the first returned result.
3. Save the original result and inspect it immediately: reference identity, complete silhouette, clipped edges, background/alpha, native and exported dimensions, UI safe space and prohibited content. Record pass/fail and preview evidence before proceeding.
4. On failure, retain the result as candidate and report the specific defect. Stop retries and image edits until the user explicitly authorizes that asset's correction. Previous approval to produce the set is not unlimited retry approval.
5. Preserve every attempt and the selected output. Crops, resizing, exports and icons derive from the selected source; they do not require imagegen. Keep native dimensions distinct from upscaled export dimensions.

## Review handoff requirements

Update README, manifest, generation history, contact sheets and validation to match actual files. Identify selected source/export paths, evidence, ready/candidate/blocked status and defects. Do not claim technical or visual checks that have not been performed. If historical rejected output is unavailable, record that gap rather than inventing attempt evidence.

Scope remains assets/art/adventure only. Preserve unrelated work in the shared checkout. No gameplay or canonical document edits. Existing permission for asset delivery to dev does not authorize main, deployment or force push.
