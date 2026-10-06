# Adventure asset preparation — inspected existing delivery

Generation is stopped. Read [HANDOFF.md](HANDOFF.md) and the `generation_policy` in [production-prompts.json](production-prompts.json) before any future work. Existing files, selected outputs and history must be checked before a request. A failed result stays Candidate; correction needs explicit approval for that asset. This audit made zero imagegen/image-edit calls.

## Actual delivery

| Group | Exists | Ready | Candidate | Blocked |
|---|---:|---:|---:|---:|
| Primary artwork | 14 | 11 | 3 | 0 |
| UI SVG | 21 | 21 | 0 | 0 |
| Stage thumbnails | 24 | 24 | 0 | 0 |
| Derived identity icons | 8 | 6 | 2 | 0 |

Ready means usable standalone asset preparation after inspection. It does not mean canonical approval or verified runtime integration. All 45 SVG/thumbnail files from delivery 01 retain their SHA-256 hashes. No gameplay, runtime UI, card data, canonical documents, rewards, save system or AI was changed.

## Selected source and export

[asset-manifest.json](asset-manifest.json) records exact source/export paths, dimensions, hashes, transforms and icon crop rectangles. [generation-log.json](previews/generation-log.json) preserves selected exact prompts and 21 historical attempts. Earlier rejected originals remain at their recorded local imagegen paths; they are not duplicated as new production assets. Some first-attempt exact prompts were not retained: this gap is explicitly recorded. Fourteen selected native originals are retained in this repository.

- Map: `maps/living-atlas-v2-source.png` → `maps/living-atlas-v2.webp`. The earlier style proof remains history and must not be treated as another missing map.
- Eight characters: `characters/*-source.png` → corresponding `.png`; 1024×1536 native and delivery, uniform content reduction with transparent padding. Alpha is real, including zero-alpha border pixels.
- Modes and scenes: `*-source.png` → `.webp`, native dimensions recorded individually; 1920×1080 delivery uses uniform upscale and a small centered aspect trim.
- Eight icons: `characters/icons/*.webp`, 256×256, cropped from the selected character sources without generation. Reviewed at 256, 96 and 64px. Source, export and icon are derivatives of one selected artwork.

## Candidate limitations — no automatic repair

- Living Atlas: native 887×1774, export 2048×4096 is an upscale. The lower prologue/puzzle placements overlap detailed relic imagery in the [24-node preview](previews/atlas-v2-24-node-review.jpg). Final runtime nameplates and routes remain untested. The overlay exists only in this preview, never in production art.
- Eira: elderly deep-brown skin, gray braids, barkcloth and staff match the user-approved proposal, but her face remains Candidate because no locked face exists. W02 supplies material direction only. Her derived icon inherits Candidate.
- Fractured Host: isolated faceless F03-based design passes technical checks; gold seams and floating fragments need human continuity review. Its icon inherits Candidate. No new power or canon is established.

## References and story decisions

Existing embedded art remains the identity reference: Liora, BS1/Aurel Veyr, GS2/Nym Avar, FS1/Varkesh Thane, WS2/Orun-Kael, F03/Fractured Host and G03/Seris Vale. Reference images are preserved under `previews/references`. Varkesh uses the existing helmet; Orun uses an amber bark knot rather than a human face. Adventure roles were approved by the user, not added as new canon.

The ending points toward **Whisperglass Relay**, a known Landmark selected under the user's discretion. It does not reveal the seventh site or move Act V's reveal. Artwork Bible V1.0 and Lore Bible V1.2 remain Candidate documents; the Card Visual CORE LOCK governs card art and was not modified.

## Review evidence

- [All 14 selected artworks](previews/current-primary-review.jpg)
- [Eight characters on light/dark backgrounds](previews/character-alpha-review.jpg)
- [Eight identity icons at multiple sizes](previews/face-icons-review.jpg)
- [Validation and unchanged-file hashes](previews/validation-report.json)
- [Actual file inventory](previews/file-inventory.json)
- [Original UI sheet](previews/ui-contact-sheet.jpg) and [stage thumbnail sheet](previews/stage-contact-sheet.jpg)

No runtime test is claimed: this delivery only prepares standalone files. Generation remains stopped; all 14 primary outputs exist and old blocked entries cannot justify another request.
