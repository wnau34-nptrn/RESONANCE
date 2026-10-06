# WONDERBOUND: RESONANCE — CARD VISUAL & ARTWORK CORE LOCK V2.0

> **Status: CORE LOCK**  
> **Current Runtime Reference:** `WONDERBOUND_RESONANCE_R5_PHASE4_2S3B_2M12_11_4_STEP4_TARGETING_READABILITY_CANDIDATE.html`  
> **Scope:** Card visual anatomy, artwork production, artwork composition, focal placement, crop safety, cross-context framing, and presentation content budget.  
> **Gameplay Impact:** NONE. This document does not change Cost, Requirement, AT/HP, card effects, balance, Resonance, combat, turn flow, AI, or Landmark rules.
>
> This lock consolidates the existing **Card Artwork Standard V1** and visual portions of **Card Presentation Core Lock V1.1**, then adds numeric focal/composition rules required by the current M12.11.4 runtime. Where this document adds new numeric focus zones, those are new V2.0 visual locks derived from the current runtime crop behavior.

---

## 1. CORE PRINCIPLE

A card must remain recognizable and tactically readable in every place where the same artwork appears:

- Hand
- Battlefield
- Card Detail
- Mulligan
- Graveyard
- Permanent / Artifact Rail
- Deck / Collection presentation

The production rule is:

> **ONE MASTER ARTWORK → MANY SAFE CROPS**

Do not solve routine framing problems by tuning every card individually.

> **Standard first. Focal override only by exception.**

---

# 2. CANONICAL CARD ANATOMY — CORE LOCK

## 2.1 Every card has exactly one primary instance of

1. **Artwork** — 1 master illustration
2. **Cost area** — 1
3. **Requirement area** — 1 area; may represent the card's required READY Resonance values
4. **Card Type** — 1
5. **Card Name** — 1
6. **Core Rule area** — 1 primary rules container

## 2.2 Optional / type-specific elements

### Creature
- **AT / HP pair** — exactly 1 pair
- **Activated Ability area** — 0 or 1
- Combat / tactical state is UI overlay/state, not part of the illustration

### Sorcery
- No AT / HP footer
- Rule/result text lives in the Core Rule area

### Equipment
- No Creature AT / HP unless a future explicit gameplay rule unlocks it
- Equipment identity must be readable from the artwork itself

### Artifact
- No Creature AT / HP
- Counter / Lightmark / Shard state is runtime UI and must not be baked into the artwork

---

# 3. CARD CONTENT BUDGET — PRESENTATION LOCK

This is a **presentation budget**, not a balance limit.

## Hand

The Hand is the primary scan surface.

- 1 Core Rule container
- Up to **3 semantic rule rows** in the Hand summary before wording must be compressed using the established card notation system
- 0 or 1 Activated Ability presentation
- Do not add extra nested boxes to fit more text
- Do not shrink essential gameplay text below the locked readability floor
- If a card has more information than the Hand can comfortably display, Hand shows the compact canonical summary and Card Detail carries the full explanation

## Card Detail

Card Detail may show the complete rule set in sections.

It must not alter the card's gameplay meaning to match Hand length.

---

# 4. ARTWORK MASTER — HARD LOCK

## Production Master

- **2048 × 1152 px**
- **16:9 landscape**
- RGB
- High-quality master retained before web compression

## Runtime Export

Default web asset:

- **1280 × 720 px WebP**
- Quality target: **80–88**

Allowed for unusually detailed illustration:

- **1600 × 900 px WebP**

## Never bake into artwork

- Card frame
- Cost
- Requirement
- AT / HP
- Card Name
- Rules text
- READY / EXHAUSTED
- GUARDIAN / HASTE / RIFTSTRIKE badges
- Lightmark / Shard counters
- Targeting rings
- Damage / trigger FX
- Any gameplay UI

Artwork is illustration only.

---

# 5. WHY 16:9 IS LOCKED

The runtime does **not** display the art at one fixed ratio.

Current M12.11.4 presentation includes approximately:

| Context | Approximate visible crop behavior |
|---|---|
| Card Detail | Near **16:9** cinematic crop |
| Desktop Hand | Very wide slice, roughly **3.2:1–4.0:1** depending on viewport |
| Mobile Hand | Very wide tactical slice, also roughly **3.2:1–4.0:1** |
| Battlefield | Variable crop depending on board density and viewport |
| Permanent / Artifact thumbnail | Can approach **1:1** |

Therefore:

> The artwork source stays 16:9, but the composition must be designed for heavy crop variation.

Do **not** compose a card as if the full 16:9 image will always be visible.

---

# 6. ARTWORK COMPOSITION ZONES — CORE LOCK V2.0

All percentages are measured from the top-left of the 16:9 master.

## 6.1 PRIMARY FOCUS POINT

The single most important identity point of the illustration.

Examples:

- Creature face / head / eye cluster
- Signature weapon + hand interaction if that defines the Creature
- Artifact object core
- Equipment object core
- Main magical collision / spell event

The Primary Focus Point must stay close to the defined anchor for the card type.

## 6.2 CORE FOCUS ZONE — NEW V2.0 LOCK

**Horizontal:** 35%–65%  
**Vertical:** 28%–58%

This is the most crop-resistant zone in the current runtime.

The **Primary Focus Point must be inside this zone** unless an intentional composition receives a focal override exception.

For a 2048 × 1152 master this equals approximately:

- X: **717–1331 px**
- Y: **323–668 px**

## 6.3 CRITICAL SUBJECT SAFE ZONE — EXISTING LOCK

**Horizontal:** 10%–90%  
**Vertical:** 16%–84%

For 2048 × 1152:

- X: **205–1843 px**
- Y: **184–968 px**

Everything required to recognize the card must remain inside this area.

This includes:

- Creature head / face / identity silhouette
- Signature weapon or identity object
- Artifact core
- Equipment core
- Sorcery impact point

## 6.4 OUTER BLEED ZONE

Areas outside the Critical Subject Safe Zone are expendable crop space.

Use them for:

- environment
- mist
- particles
- secondary architecture
- trailing cloth
- secondary limbs
- ambient magic
- decorative foreground/background

No card identity may depend on the outer bleed zone.

---

# 7. DEFAULT FOCUS ANCHOR BY CARD TYPE — CORE LOCK V2.0

These are production targets, not per-card CSS overrides.

| Card Type | Default Primary Focus Anchor | Preferred Range |
|---|---:|---:|
| **Creature** | **X 50% / Y 36%** | X 40–60% / Y 32–42% |
| **Artifact** | **X 50% / Y 50%** | X 42–58% / Y 42–58% |
| **Equipment** | **X 50% / Y 48%** | X 42–58% / Y 38–58% |
| **Sorcery** | **X 50% / Y 45%** | X 35–65% / Y 35–55% |

Approximate 2048 × 1152 pixel anchors:

- Creature: **1024, 415**
- Artifact: **1024, 576**
- Equipment: **1024, 553**
- Sorcery: **1024, 518**

---

# 8. CREATURE ARTWORK — HARD LOCK

Creature art must communicate identity in approximately one second.

## Required composition

- Head / identity region sits around **32%–42% from the top** of the master
- Default head/facial focus target: approximately **X 50% / Y 36%**
- Upper body or defining silhouette occupies the central band
- Key weapon / horns / wings / magical identity may extend outward, but the identity-defining portion remains within the Critical Subject Safe Zone
- Background must separate the silhouette clearly

## Strong recommendation

The most important facial / identity information should stay roughly within:

- X 40%–60%
- Y 30%–48%

This survives the current Hand and Battlefield upper-middle framing significantly better than a low-centered portrait.

## Avoid

- Head near the top edge
- Face below ~55% of the canvas
- Full-body composition where the face becomes tiny
- Identity depending on feet / lower weapon tip / bottom 20% of the image
- Large empty upper area with the Creature pushed into the bottom third
- Critical weapon entirely at extreme left/right edge

## Large / non-humanoid Creatures

If there is no human-like face, use the equivalent identity focus:

- eye cluster
- mask
- glowing core
- horn crown
- maw
- emblem

Place that identity point using the same Creature focus anchor system.

---

# 9. ARTIFACT ARTWORK — HARD LOCK

Artifact art must survive a very small Permanent thumbnail.

## Composition

- Main object close to **X 50% / Y 50%**
- Object must be recognizable without reading surrounding environment
- Keep negative space around the object
- Use clear shape separation and a distinct silhouette

## Avoid

- Multiple equal-priority objects
- Important inscription/detail near frame edges
- Object filling 100% of the frame
- Tiny artifact placed inside a huge environment shot

The artifact must still read when cropped near 1:1 at approximately 24–30 px runtime size.

---

# 10. EQUIPMENT ARTWORK — HARD LOCK

Equipment follows Artifact crop rules, but the image must immediately read as something that can be:

- worn
- held
- attached
- equipped

Default focus:

**X 50% / Y 48%**

The usable object is always visually stronger than the background.

---

# 11. SORCERY ARTWORK — HARD LOCK

The focal subject is the **event**, not necessarily a character.

Examples:

- magical collision
- beam
- rupture
- restoration
- summoning event
- environmental transformation

Default action focus:

**X 50% / Y 45%**

The critical magical event must remain inside the Core Focus Zone.

If a character appears, the character supports the event composition rather than becoming a portrait that pushes the actual effect to the edge.

---

# 12. CONTRAST & READABILITY AROUND THE FOCUS — V2.0 LOCK

The focal subject must remain readable at thumbnail scale.

Around the Primary Focus Point:

- maintain clear luminance or color separation from the background
- avoid background detail with equal visual weight
- preserve a readable silhouette
- do not hide the face / object core in bloom, fog, debris, or particle noise

The image may be dark and atmospheric, but the focal identity itself must not disappear when the image is reduced to Hand or Battlefield size.

---

# 13. CROPPING RULES BY UI CONTEXT

## Hand

Hand is the most aggressive vertical crop.

Production artwork must remain identifiable from a very wide horizontal slice.

Priority:

1. Face / object core
2. Signature silhouette
3. Key action
4. Background story

If only the environment survives but the subject is lost, the artwork fails.

## Battlefield

Priority:

1. Creature identity
2. Tactical silhouette
3. Head / core object

READY / EXHAUSTED / TARGET / SOURCE / Ability state must be communicated by UI, not by alternate art.

## Card Detail

Card Detail is the cinematic viewing context.

It should reveal the intended wider scene and reward inspection, but the composition must still be based on the same master art.

## Permanent Rail

Artifact/Equipment must be readable at thumbnail scale from the center crop.

## Mulligan / Graveyard / Deck

Reuse the same master artwork and standard framing system.

Do not create a unique crop manually for every card as the default workflow.

---

# 14. ART FOCUS OVERRIDE — EXCEPTION ONLY

Runtime focal override may exist for exceptional legacy or intentionally asymmetric artwork.

Use only when:

- a legacy image predates this standard
- a deliberate cinematic composition cannot follow the standard anchor
- the card remains visually stronger with an intentional exception

Do not use focal override to compensate for poor production composition.

## Quality Gate

If more than approximately **10% of a set** needs per-card focal override:

> The artwork production guideline or context framing preset is wrong and must be corrected.

Do not continue adding card-by-card overrides.

---

# 15. CARD FRAME / ARTWORK RESPONSIBILITY SPLIT — HARD LOCK

## Artwork owns

- fantasy subject
- environment
- storytelling
- atmosphere
- lighting
- visual identity

## UI owns

- Cost
- Requirement
- Card Type
- Card Name
- Rules
- AT / HP
- Ability state
- Combat state
- Keywords / badges
- Counters
- Targeting
- Damage
- Trigger results
- selection / hover state

Never paint gameplay state directly into the illustration.

---

# 16. CURRENT RUNTIME ART WINDOWS — REFERENCE, NOT SOURCE-ASSET LOCK

These values explain why the focal rules exist. They may change in future responsive tuning without changing the 16:9 source standard.

## Desktop Hand — current M12.11.4

Normal viewport:

- Hand Card height: about **292 px**
- Artwork window height: about **68 px**

Short desktop:

- Card height: about **254 px**
- Artwork: about **60 px**

Very short desktop:

- Card height: about **226 px**
- Artwork: about **56 px**

Typical card width remains around the low-200 px range, creating a highly panoramic visible crop.

## Mobile Hand

Mobile Hand uses a compact tactical tile rather than the full desktop Card layout.

Artwork remains a wide shallow crop.

## Card Detail

Normal Detail uses a **16:9 art region** before responsive landscape variants.

## Permanent Rail

Current desktop art thumbnail is approximately **24–26 px square** inside a 28–30 px item height.

---

# 17. ARTWORK GENERATION PROMPT STANDARD

Base prompt:

> Fantasy card artwork for WONDERBOUND: RESONANCE, cinematic 16:9 landscape composition, [CARD SUBJECT / ACTION], dark fantasy world of Caldris, premium collectible card game illustration, clear primary focal subject, strong readable silhouette, atmospheric depth, generous crop-safe environment around all edges, critical identity fully contained inside the central safe area, no text, no typography, no card frame, no UI, no icons.

## Creature add-on

> Primary identity focus around x50% y36% of the frame, head/face in the upper-middle region around 32–42% from the top, upper-body identity clearly readable, key weapon and head remain crop-safe, subject separated clearly from the background.

## Artifact add-on

> Primary object centered around x50% y50%, object fully readable at thumbnail scale, clean silhouette, generous negative space, no critical details near outer edges.

## Equipment add-on

> Equippable object centered around x50% y48%, visually dominant over the environment, clear usable form, generous crop-safe negative space.

## Sorcery add-on

> Magical event is the primary focal point around x50% y45%, action remains inside the crop-safe center, dynamic scene with expendable atmosphere and particles around the outer edges.

---

# 18. ARTWORK ACCEPTANCE GATE — MUST PASS

A new production artwork passes only when all applicable checks pass.

## Source

- [ ] 2048 × 1152 px
- [ ] 16:9
- [ ] no card frame / UI / typography baked in

## Composition

- [ ] Primary Focus Point is inside the correct type-specific range
- [ ] Critical identity remains inside X 10–90% / Y 16–84%
- [ ] Main focal subject remains readable in the Core Focus Zone
- [ ] Outer edges can be cropped without destroying identity

## Hand Test

- [ ] A very wide ~3.5:1 center/upper-middle crop still identifies the card immediately
- [ ] Creature face / object / spell event is not cut away

## Battlefield Test

- [ ] Creature identity is readable at small size
- [ ] Key silhouette survives dense-board crop
- [ ] Artwork does not require READY/EXHAUSTED-specific alternate art

## Detail Test

- [ ] 16:9 presentation still feels intentionally composed and cinematic

## Permanent Test

For Artifact / Equipment:

- [ ] near-1:1 central thumbnail still identifies the object

## System Test

- [ ] no per-card focal override required under normal circumstances
- [ ] if an override is required, it is documented as an exception

---

# 19. LEGACY ART MIGRATION

Current legacy 512 × 512 assets may remain during prototype development.

Migration order:

1. Keep existing assets using runtime framing presets
2. Do not regenerate every card only to satisfy prototype polish
3. All **new production artwork** follows this V2.0 lock immediately
4. Replace legacy art family-by-family / expansion-by-expansion
5. Keeper portrait uses a separate portrait asset in production rather than forcing the 16:9 card art to serve as the portrait master

---

# 20. KEEPER PORTRAIT — SEPARATE ASSET LOCK

Keeper Portrait is not a normal card-art crop target in production.

Recommended portrait master:

- **1:1** or **4:5**

Do not require every 16:9 Card Artwork to double as a Keeper portrait.

---

# 21. CHANGE CONTROL

This is a **Core Lock**.

Future work must not silently change:

- 2048 × 1152 production master
- 16:9 source ratio
- Critical Subject Safe Zone
- Core Focus Zone
- type-specific default focus anchors
- no-UI-baked-into-art rule
- standard-first / override-by-exception policy
- one master artwork serving multiple UI contexts
- Artifact/Equipment thumbnail readability requirement

Any intentional change requires an explicit **Core Unlock / V2.x revision**.

---

# 22. ONE-PAGE ART DIRECTOR SUMMARY

## MASTER

**2048 × 1152 · 16:9**

## CRITICAL SAFE ZONE

**X 10–90% · Y 16–84%**

## CORE FOCUS ZONE

**X 35–65% · Y 28–58%**

## DEFAULT FOCUS

- Creature → **50 / 36**
- Artifact → **50 / 50**
- Equipment → **50 / 48**
- Sorcery → **50 / 45**

## CREATURE HEAD

Target around **32–42% from top**

## ART MUST SURVIVE

- ~3.2–4.0:1 Hand crop
- variable Battlefield crop
- 16:9 Detail
- near-1:1 Permanent thumbnail

## NEVER BAKE IN

Text / frame / Cost / Requirement / AT-HP / state / counters / targeting / FX

## OVERRIDE

Exception only. If >10% of a set needs override, fix the art pipeline.

---

**WONDERBOUND: RESONANCE — CARD VISUAL & ARTWORK CORE LOCK V2.0**  
**Status: CORE LOCK**
