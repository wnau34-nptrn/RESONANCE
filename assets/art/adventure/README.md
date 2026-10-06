# Adventure asset preparation — delivery 01

Partial delivery for WONDERBOUND: RESONANCE. **1 of 14 primary artworks produced (Atlas style proof, candidate), 21 ready SVG assets, 24 ready derived stage thumbnails.** The other 13 primary artworks await the requested first-style-proof approval. No transparent character artwork or generated face icons are delivered yet. No game files, card data, artFocus, combat, rewards, saves, or runtime UI were changed.

`ready` means the file has passed the applicable technical and visual checks and is available for later integration review. It does not promote a production candidate into lore or visual canon, assign reward thresholds, or authorize integration. `candidate` is a produced file requiring the stated review. `blocked` has no file; target dimensions are proposals, not claims of completed delivery.

## Sources and authority

- Fetched `origin` and started `codex/adventure-assets` from `origin/dev` at `a58ba782a53ec307da214d55e0afda228bc78681`.
- [Artwork Bible V1.0](../../../docs/art/WONDERBOUND_RESONANCE_ARTWORK_BIBLE_V1_0.md): **Visual Production Candidate**, including appearance/material proposals.
- [Lore Bible V1.2](../../../docs/lore/WONDERBOUND_RESONANCE_COMPLETE_LORE_BIBLE_V1_2.md): **Lore Canon Candidate**. Source-derived facts remain attributed to this document; no automatic canon promotion.
- [Card Visual Core Lock V2.0](../../../docs/art/WONDERBOUND_RESONANCE_CARD_VISUAL_ARTWORK_CORE_LOCK_V2_0.md): **CORE LOCK**, for card artwork and its crops. New dialogue portraits and map assets have separate proposed sizes.
- Existing world, six Landmark images, 48 card artworks, and Liora's keeper image were inspected in [existing-reference-sheet.jpg](previews/existing-reference-sheet.jpg). Retained reference exports are exact embedded WebP bytes from `index.html`; their dimensions/hashes are in [reference-inventory.json](previews/reference-inventory.json). They are reference material, not newly produced primary artworks.

## Confirmed Adventure cast and scene choice

The user confirmed these Adventure production roles in this chat; the assignment is **not a new lore-canon declaration**:

| Role | Identity | Existing visual reference |
|---|---|---|
| Beacon miniboss | Echo of Aurel Veyr | BS1 |
| Glasswind miniboss | Echo of Nym Avar | GS2 |
| Fracture miniboss | Varkesh Thane | FS1 |
| Wildroot miniboss | Orun-Kael | WS2; preserve colossal nonhumanoid scale |
| Act I boss | The Fractured Host | Existing keeper alias uses F03 |
| Supporting NPC | Seris Vale | G03 |
| Supporting NPC | Eira Mossborn | W02 is a Rootkeeper **order** illustration, not a verified Eira face |

Opening scene: Liora discovers a Living Atlas Fragment, supported by Lore section 17. Ending scene: the user chose a route to a **known Landmark**, preserving the Lore chronology and excluding a seventh-site reveal. The particular known Landmark still needs selection before that scene is produced.

## Differences found and production boundaries

1. Existing Liora art has long brown hair, ivory clothing, ornate teal mantle, and a lantern. Artwork Bible section 5 proposes shoulder-length hair, an expedition coat, and bracer as a candidate. The user's preservation instruction takes precedence: future dialogue art must retain the existing reference identity and clothing. No redesign was produced.
2. Current Adventure `c2` reveals a seventh site, whereas Lore reserves it for Act V. The user chose the known-Landmark ending for this asset package. Runtime was not changed.
3. The existing Fractured Host keeper aliases the F03 Crackseer art. Preserve its existing face/silhouette for continuity review; do not treat all F03 lore as the Host's biography.
4. W02 depicts the Rootkeeper order and cannot by itself establish Eira's facial identity. Use it for material/style only; a proposed elder appearance from the Artwork Bible remains a candidate requiring review.
5. Existing forge art has warm, fire-like light while Lore says the Forge has no conventional fire. It was inspected, not altered, and is not used for new literal scene production in this delivery.

## Files and use

- [asset-manifest.json](asset-manifest.json): all 59 requested primary/UI/thumbnail entries, actual file sizes/hashes, source dimensions, crop rectangles, and per-item status. Blocked entries have null paths and null actual dimensions.
- `maps/`: original 887 × 1774 RGB imagegen style proof and 2048 × 4096 WebP export. **The export is a uniform upscale, not a native 2K × 4K master.** No distortion. Both remain candidate review material.
- `nodes/stage-*.webp`: 24 RGB 512 × 512 crops from existing art, quality 85. Stage IDs match the existing 6 prologue + 12 Resonance + 2 convergence + 4 puzzle stages. Images are associations for the stage, not new claims of literal geography. No new source image was generated for these crops.
- `nodes/*.svg`: six stage-type icons and four independent stage-state frames, 128 × 128 viewBox.
- `rewards/*.svg`: bronze/silver/gold stage medals, one Act I medal, four Resonance miniboss badges, and three reward-choice frames. Icons/medals are 128 × 128; reward frames are 512 × 720. No external dependencies, fonts, scripts, or currency design.
- `previews/*-render.png`: actual standalone SVG renders used for alpha/visual checks.
- `characters/`, `modes/`, `scenes/`: no production files yet; their required entries remain blocked in the manifest.

Recommended SVG display: icons/medals at 48px or larger (reviewed at 32px); reward frames at widths of 220px or larger. SVG state markers use geometry as well as color. Layer the separate frame around a stage image; preserve its full viewBox. Reward-frame centers remain transparent for existing reward art.

## Composition and crop guidance

The map is an **abstract symbolic Atlas surface**, not a canonical geographic map. Lower band is introductory, middle has four Resonance visual areas, upper band is convergence. Review [24-node layout](previews/atlas-24-node-layout-review.jpg) and [normalized coordinates](previews/layout-review.json). Labels and circles exist only on this review preview. Production map artwork contains no stage markers, unlock states, UI connectors, labels, buttons, or watermark. Architectural bridges and the relic's material engraving are scenery, not route definitions.

The generated middle/upper areas are more detailed than the requested quiet-overlay target. Use the review to approve or request more low-detail space before calling the map ready. Keep nameplates on separate opaque/translucent UI surfaces, not painted into the background. The 24-node preview verifies placement feasibility, not mobile touch-target sizing or a final tree layout. Future responsive layouts should crop/scroll sections rather than shrink the entire tall map to a narrow screen.

Each thumbnail records source-pixel crop bounds from the top-left. Use the delivered crop unchanged initially; evaluate at 64px/96px. Repeated source artwork is intentional. These thumbnail exports do not modify the game's existing card master, source asset, or runtime focal settings.

If later producing **card artwork**, retain 2048 × 1152 masters and use Core Lock safe zones: critical X10–90% / Y16–84%, focus X35–65% / Y28–58%; Creature anchor 50/36, Artifact 50/50, Equipment 50/48, Sorcery 50/45. This delivery contains no newly generated card artwork.

Proposed dialogue assets: 1024 × 1536 transparent PNG, complete character with clear outer margins and face/upper torso suitable for half-body and 96px face-icon crops. Orun-Kael must keep a nonhuman awareness silhouette and scale cues rather than receive a human face. Proposed modes/scenes: 1920 × 1080 with separate UI dialogue space. Record original and exported dimensions separately; do not stretch outputs.

## Review contact sheets

- [Primary artwork inventory](previews/artwork-contact-sheet.jpg): one candidate and thirteen clearly marked missing artworks.
- [Character references](previews/character-contact-sheet.jpg): reference-only, **zero new portraits**.
- [UI and medals](previews/ui-contact-sheet.jpg): every SVG, large and 32px previews.
- [24 stage thumbnails](previews/stage-contact-sheet.jpg): every crop, large and actual 64px previews.
- [Standalone preview page](previews/index.html): opens without changing the game.
- [Validation report](previews/validation-report.json): actual dimensions, hashes, alpha, SVG dependency checks, and scope results.

## Remaining gates before production/integration

- Approve or revise the first Atlas visual-language proof before repeated raster production.
- Review map density and native-resolution limit; request a higher-detail native master if needed.
- Choose the known Landmark for the ending shot; do not introduce new sites or resolve canon mysteries.
- Verify an Eira appearance proposal and the F03-to-Host continuity interpretation before their portrait production.
- Produce and visually inspect the remaining thirteen artworks, genuine character alpha/edges, full/half-body crops, and face icons; no alpha check is claimed for absent characters.
- Approve SVG designs and thumbnail-stage associations for final integration. Medals/badges define no new reward mechanics.
- Select layout, scrolling, accessibility text, route edges, status overlays, and reward selection behavior in the later development task. This package implements none of those systems.

Generation used the built-in imagegen tool. The exact first-proof prompt is retained in [production-prompts.json](production-prompts.json).
