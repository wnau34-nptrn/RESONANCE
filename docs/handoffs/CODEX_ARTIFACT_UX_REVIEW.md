# Codex review → Antigravity: Artifact UX revision required

วันที่: 2026-10-07
ผล: HOLD — ยังไม่ผ่าน acceptance สำหรับนำเข้า Dev/Main

## Baseline และขอบเขต

HEAD `4a94b290848e2a25a08ae67c9efb2394f7c69eca`.
Reviewed index SHA-256 `a31af9e9107a022b5679365873931ed9ba8cdbed4d79618b0f176ff8478c643f`.
Implementation diff ที่ตรวจจริง: `index.html` +282/-3 บรรทัด; RETURN ระบุ +285/-3 จึงควรปรับตัวเลขให้ตรง delta ปัจจุบัน

Codex ตรวจ code, ภาพส่งกลับ และ browser แยกที่เปิดผ่าน local HTTP บน Chrome ไม่มีการแก้ implementation, stage, commit, push หรือ deploy ในรอบ review นี้

## Findings ตามลำดับความสำคัญ

### [P1] Mobile ตัดสรุปและสถานะ Artifact ออกจริง

ที่ 844×390 มี tile ผู้เล่น x=770, width=66px แต่ Atlas status เริ่มที่ x=942.33, width=75.53px จึงอยู่นอก tile/viewport และถูก overflow ตัดทิ้ง Bastion status เริ่มที่ x=975.67 เช่นกัน

Computed style: `.permanent-copy` กลายเป็น `display:block` และ `.artifact-summary` เป็น `display:inline` ทำให้ summary กับ status ต่อกันในบรรทัดเดียว แทน layout สามบรรทัดที่ CSS ใหม่ตั้งใจไว้ แม้ tile สูง 34px แล้วก็ตาม การทดสอบเพียงความสูง/ไม่มี page overflow จึงไม่ยืนยันว่าข้อมูลอ่านได้

Owner: scoped Artifact CSS/cascade ประมาณ 41153–41231 และ legacy mobile rules ที่ชนะ display ของ descendant.

แก้เฉพาะ Artifact descendants ให้ layout ถูกต้องตาม cascade จริง พื้นที่มือถือแคบมาก จึงอาจใช้ icon + status ย่อ และให้แตะอ่านเต็มตาม handoff ห้ามขยาย battlefield/Creature หรือย่อข้อความจนอ่านไม่ได้ ตรวจ bounds ของ summary/status เทียบ tile และ screenshot จริง ทั้งสองฝั่ง 844×390/667×375 และมือขยาย/หด

หลักฐาน Codex: `C:\Users\Warunyu.N\.codex\visualizations\2026\10\05\01a10a2c-621b-7ee0-894b-55863a750b1c\artifact-ux-review\mobile-current.png`.

### [P2] Edge of Ruin / Ancient Canopy บอกว่าพร้อมทำงานหลังใช้ครบแล้ว

`WB_ARTIFACT_DEFS.edgeRuin.status()` และ `.canopy.status()` ประมาณ 29388–29397 คืน passive/พร้อมทำงานเสมอ ไม่อ่านตัวจำกัดครั้งใน V2.4.

Final engine จำกัดด้วย instance `a.p3cOnce.B24_FS2` และ `a.p3cOnce.B24_W07` เทียบ `game.p3cTurnSerial` (ประมาณ 39373–39380).

Codex เรียก display helper กับ instance ที่ทั้งสอง key เท่ากับ turn serial 7: ทั้งสองยังคืน `state:passive` และ desc ว่า `พร้อมทำงาน…` จึงยืนยันผิดจากสถานะ used ตาม handoff.

แก้ read-only mapping ให้ตรง final runtime keys ต่อ UID และทั้งสองเจ้าของ ตรวจ used → next-turn reset อย่าเรียก p3cOnce() เพื่อเช็กสถานะ และอย่าแก้ engine

### [P2] Artifact FX หายหลังเริ่ม Duel ใหม่ในหน้าเดิม

`wbPlayedArtifactFx` เป็น Set ระดับหน้า ประมาณ 32127; ใช้ `ev.id` อย่างเดียวและไม่มี reset/namespace ตาม Game instance.

Game.note เริ่ม eventSeq ใหม่ในแต่ละเกม Codex ใช้ Game สอง instance ในหน้าเดียว ตั้ง Atlas และ emit RESTORE ผ่าน engine เดิมทั้งสองครั้ง: event id=3, Atlas uid=11 เหมือนกัน เกมแรก pulse=true เกมที่สอง pulse=false เพราะ ID ค้างใน Set ของเกมแรก

แก้ presentation dedup ให้ผูกกับ Game instance/lifecycle และยังกัน replay ของ event เดิมภายในเกมเดียวได้ ตรวจ restart, เข้า Battle ใหม่, ออกกลับ map และ event หลายครั้งในเทิร์นเดียว ไม่เปลี่ยน engine ID

### [P2] Citadel FX ไม่เข้าทาง event จริง และ fallback เดา instance

Engine สร้าง event `Whisperglass Scout · Citadel Barrier 10` เป็น `fxKind:BUFF` พร้อม target UID/owner แต่ไม่มี source UID.

`p4TriggerEvents()` ประมาณ 32126 รับ TRIGGER หรือ regex บางข้อความ จึงกรอง Citadel BUFF ทิ้งก่อนถึง `wbPresentArtifactEventFx()`.

Codex เพิ่ม Citadel แล้วเรียก summon Creature ผ่าน engine เดิม: event BUFF มีจริง แต่ filtered events=[]; Citadel pulse=false; beam=false.

อีกทั้ง fallback `/Citadel/` ใน helper เลือก `.find(a.key==='citadel')` ซึ่งเดา source instance จากชื่อและเลือกใบแรก ขัดกับ handoff ที่ห้ามเดา source เมื่อ metadata ไม่พอ

แก้ภายใน presentation scope เท่านั้น ถ้า event เดิมพิสูจน์ source ไม่ได้ ให้รายงานข้อจำกัด/ใช้ feedback ที่ไม่อ้าง source ตาม handoff ห้ามเพิ่ม source metadata ด้วยการแก้ engine และห้ามแสดง beam ที่เดาต้นทาง

### [P2] PASS ของ regression ยังไม่มีหลักฐานว่าเล่นครบ acceptance

RETURN ให้ Normal Duel PASS โดยเหตุผล `กลไกเกมไม่มีการแก้ไข คงเดิม 100%` นี่เป็นหลักฐาน scope ของ diff ไม่ใช่หลักฐานว่าผ่าน mulligan/Attune/combat/AI turn จริง

Beam test ที่ส่งกลับใช้ synthetic event โดยตรง จึงยืนยัน helper ได้ แต่ไม่ยืนยันว่า event จริงทุก Artifact ถูกส่งมาถึง helper ตัวอย่าง Citadel ข้างต้นแสดงช่องว่างนี้แล้ว

ยังไม่มีหลักฐานแนบที่เพียงพอสำหรับ Echo Trials ทั้ง 4 ชนะจริงโดย et2/3 ไม่ใช้ Hint, Lore/Tutorial/Adventure return, duplicate-source feedback, FX cleanup เมื่อเปลี่ยนด่าน หรือ hover/focus tooltip ต้องระบุ NOT TESTED จนทดสอบจริง อย่าใช้คำว่า complete/pass all

## Checks ที่ผ่านใน review รอบนี้

- Hash ตรง RETURN และ delta patch reverse-check ผ่าน
- `git diff --check` ผ่าน
- Inline scripts 47 ชุด parse ผ่าน ไม่มี syntax failure
- Diff ของเกมจำกัดที่ Artifact renderer, display helpers, Artifact detail note, presentation FX และ CSS ใหม่ ไม่มี engine/card-definition hunk
- Desktop screenshot เพิ่ม effect summary และ state ได้ตามทิศทางที่ตกลง ภาพมือถือยังไม่ผ่านตาม finding ข้างต้น

ไม่มีการกล่าวอ้างว่า Safari/iOS หรือ full gameplay regression ผ่านจากการตรวจรอบนี้ การเรียก engine/display helper ใน test profile ข้างต้นเป็น targeted diagnostic ไม่ใช่หลักฐานชนะด่านผ่าน UI

## Git status ณ จบ review

```text
 M index.html
?? docs/handoffs/ANTIGRAVITY_ARTIFACT_UX_DELTA.patch
?? docs/handoffs/ANTIGRAVITY_ARTIFACT_UX_HANDOFF.md
?? docs/handoffs/ANTIGRAVITY_ARTIFACT_UX_RETURN.md
?? docs/handoffs/CODEX_ARTIFACT_UX_REVIEW.md
?? docs/handoffs/evidence-artifact-ux/
?? scratch/
```

scratch/ เป็นไฟล์ที่ Antigravity ทิ้งไว้ ไม่อยู่ในขอบเขต implementation ที่ handoff อนุญาต Codex รักษาไว้และไม่ลบ ห้าม stage รวมโดยไม่ตรวจ

## Prompt สำหรับส่งกลับ Antigravity

แก้เฉพาะ findings ใน CODEX_ARTIFACT_UX_REVIEW.md ภายใต้ ANTIGRAVITY_ARTIFACT_UX_HANDOFF.md เดิม รักษางานอื่นและ locked systems ห้าม Git actions ให้เก็บ snapshot ของงานที่รับรอบแก้ไว้ และส่ง revision delta เทียบ snapshot นั้น พร้อม cumulative delta เทียบ baseline 4a94b29 ระบุชัดเจนว่าแต่ละ patch เทียบอะไร

ปรับ RETURN ให้มี PASS/FAIL/NOT TESTED ตามหลักฐานจริง เพิ่ม before/after ของจุด mobile ที่ถูกตัด, state used ของ Canopy/Edge, FX ของสองเกมต่อกัน และ event จาก engine จริงตาม finding เมื่อแก้ครบให้ส่งกลับผู้ใช้เพื่อให้ Codex review อีกครั้งก่อน Dev/Main ห้ามถือว่าเอกสาร review นี้เป็นการอนุมัติ Git actions
