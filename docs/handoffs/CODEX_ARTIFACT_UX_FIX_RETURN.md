# Codex Artifact UX fixes

วันที่ 2026-10-07 — Working-tree implementation only; no Git actions.

## Baseline

แก้ต่อจาก Antigravity index SHA-256 `a31af9e9107a022b5679365873931ed9ba8cdbed4d79618b0f176ff8478c643f` บน HEAD `4a94b290848e2a25a08ae67c9efb2394f7c69eca`.
รักษางาน Antigravity และ scratch เดิม ไม่แก้ engine/card definitions.
รายงาน CODEX_ARTIFACT_UX_REVIEW.md เป็นผลของเวอร์ชันก่อนแก้ เอกสารนี้บันทึกผลหลังแก้เฉพาะ findings ที่ยืนยันแล้ว.

## Changes and cause

- Mobile legacy cascade เปลี่ยน permanent-copy เป็น block ทำให้ summary/status ต่อบรรทัดและหลุดนอก tile: เพิ่ม scoped mobile descendant rules; ใช้ชื่อ + ป้ายสั้น เช่น `รอผล`, `ใช้แล้ว`, `โบนัส`; ค่าตัวเลขและข้อความเต็มยังอยู่ใน modal/aria-label/title เดิม ใช้พื้นที่ Artifact เดิม ไม่แก้สนามหรือ Creature.
- Edge of Ruin และ Ancient Canopy อ่าน instance keys `B24_FS2` / `B24_W07` เทียบ turn serial เพื่อแสดง used และ reset ตามเทิร์นจริง เป็น read-only.
- FX dedup เปลี่ยน page-wide Set เป็น WeakMap ต่อ Game instance; event ไม่มี ID ใช้ identity ของ event object ป้องกันการชนจากข้อความเหมือนกัน New Duel ไม่รับ ID cache ของเกมก่อน.
- Citadel event จริงเป็น BUFF ระบุ recipient/amount แต่ไม่มี source UID: ตรวจ event รูปแบบที่ engine เดิมสร้างและแสดง `BARRIER 10` ที่ recipient เท่านั้น เพิ่มรับ event นี้ใน Artifact presentation โดยรักษา trigger cue เดิม ลบการหา Citadel ใบแรกจาก regex ไม่มี beam/source pulse ที่เดา instance และไม่แก้ engine metadata.

## Verified

- Inline scripts 47 ชุด parse ผ่าน; git diff --check ผ่าน.
- Artifact text bounds ผ่านทั้งสองเจ้าของ: 844×390, 667×375, 1024×667, 1440×900; ดู screenshot หลังแก้จริง ข้อความย่อบนมือถือและข้อมูลเต็ม desktop.
- Canopy/Edge used และ next-turn reset ทั้งสองเจ้าของผ่าน; emit event ผ่าน engine จริงยืนยัน final cap keys ได้.
- เริ่ม Game ใหม่สองครั้ง event ID ซ้ำกันยังแสดง FX ทั้งสองครั้ง; replay event เดิมในเกมเดียวไม่แสดงซ้ำ.
- Citadel สอง instance: summon Creature ผ่าน engine จริง → BUFF → target cue ถูก UID เพียงครั้งเดียวเมื่อ replay; ไม่มี source pulse หรือ beam ที่อ้างใบแรก.
- Artifact detail เปิด/ปิดผ่าน UI.
- Echo Trials et1/et2/et3/et4 ชนะผ่าน mobile touch UI โดยไม่ใช้ Hint: Equipment/payment, Omen/choice, Return/enemy target, Combat/Journey/Claim.
- ไม่พบ pageerror ในการทดสอบข้างต้น.

## Evidence and limits

Evidence folder:
`C:\Users\Warunyu.N\.codex\visualizations\2026\10\05\01a10a2c-621b-7ee0-894b-55863a750b1c\artifact-ux-fix\`

- `verify.cjs` — isolated-profile checks; fixture tests ระบุชัดเจน ไม่ใช้เป็นหลักฐานชนะ.
- `results.json` — targeted state/FX checks และ Echo Trials ทั้ง 4 ผ่าน UI จริง.
- `layout-results.json` — syntax/geometry รอบสุดท้ายหลังปรับป้ายมือถือ.
- `fixed-844x390.png`, `fixed-667x375.png`, `fixed-1024x667.png`, `fixed-1440x900.png`.
- `et1-win.png` ถึง `et4-win.png`.

Citadel ยังไม่มี source beam/pulse เพราะ engine ไม่ระบุต้นทาง แสดงเฉพาะผลบน Creature ตามข้อมูลจริง.
ไม่ได้ทดสอบ Safari/iOS เครื่องจริงหรือบอสทุกด่าน; ไม่อ้างว่า comprehensive gameplay regression ของทุก Artifact/Normal Duel/Lore/Tutorial ผ่านทั้งหมด.

ยังไม่ได้ stage/commit/push/deploy. index.html และไฟล์ส่งกลับเดิมยังเป็น working-tree changes ตามเดิม.
