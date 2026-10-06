# Antigravity → Codex: Adventure bug-fix handoff

วันที่: 2026-10-06
สถานะ: อนุญาตให้แก้เฉพาะสอง bug ด้านล่าง แล้วส่งกลับ Codex ตรวจสอบก่อนนำเข้า Dev

## Prompt สำหรับ Antigravity

คุณได้รับมอบหมายให้แก้ P1 และ P2 ที่ Codex ตรวจพบใน WONDERBOUND: RESONANCE ตามรายละเอียดในเอกสารนี้ ทำงานบน working tree ปัจจุบัน ไม่ย้อนกลับไปใช้ HEAD เพราะมีงาน Adventure Tree/Lore และคู่มือที่ยังไม่ commit อยู่แล้ว อ่าน AGENTS.md และ GEMINI.md ก่อนเริ่ม ตรวจ implementation และ reproduce ก่อนแก้ ใช้ minimum diff ที่ owner ของแต่ละ bug เท่านั้น

ห้าม stage, branch, commit, push, merge, สร้าง PR หรือ deploy รวมถึงห้ามนำเข้า dev/main งานรอบนี้จบที่การส่ง patch และผลทดสอบกลับให้ Codex รีวิว ไม่จบที่การนำขึ้น GitHub ไม่แก้ปัญหาอื่นที่พบระหว่างทาง ให้รายงานแยก ห้ามสร้างหรือแก้รูปด้วย imagegen

## Workspace และสถานะรับงาน

- Repository: `D:\My Drive\AI\Project Game\Resonance\GITHUB\RESONANCE`
- HEAD ณ ส่งงาน: `d7be81e8988b4145cdb3881775af17f6159159ed`
- Branch ปัจจุบัน: `codex/adventure-assets` ใช้ checkout เดิม; ไม่เปลี่ยน branch
- งาน Codex ที่มีอยู่ก่อนรับงาน: modified `index.html` และ `assets/art/adventure/previews/validation-report.json` ต้องรักษาทั้งหมด
- `index.html` SHA-256 ก่อนแก้ bug: `20090de9912855bc4b48cffed6b0f86b3e815c53e9b72aefb7efd7bc2add2700`
- `validation-report.json` SHA-256: `b58c0f1394e04d47e5485f8c99a81ed1b2208e689fb27b51ff8111354a31436d` ห้ามแก้ไฟล์นี้ในงาน bug-fix

ก่อนเริ่ม ตรวจ git status และเก็บ snapshot/diff ของ working tree ที่รับมาไว้นอก repository เพื่อแยก delta ของคุณออกจากงาน Codex หาก hash เปลี่ยนเพราะมีงานใหม่ ให้ตรวจการเปลี่ยนแปลงและบันทึก baseline ใหม่ ห้าม reset, clean, checkout ทับ หรือ restore งานที่มีอยู่

## P1 — หน้าต่างเลือกเป้าหมายไม่แสดงหลังเล่น Sorcery

ผลกระทบ: ปริศนา Echo Trials 2–3 เล่นต่อตาม flow ปกติไม่ได้ เพราะเกมรอ choice แต่ผู้เล่นไม่มีหน้าต่างให้เลือก

ขั้นตอน reproduce:

1. เปิด Adventure → Basic → Echo Trials 2 “ราคาของชัยชนะ”
2. แตะ Omen of Collapse ในมือ แล้วกดเล่นการ์ด
3. Detail ปิด แต่ไม่มีหน้าต่างเลือก Creature เพื่อสังเวย
4. `game.pendingChoice.type` เป็น `p23_prepare_play`; DOM ไม่มี `[data-p3d-choice-layer]`
5. อาการเดียวกันเกิดใน Echo Trials 3 “ถอยเพื่อเปิดทาง” เมื่อเล่น Return Through Glass

Codex reproduce บน baseline d7be81e แล้ว จึงเป็น bug เดิม ไม่ใช่ regression ที่เกิดจาก Adventure Tree

สาเหตุที่ยืนยัน:

- `beginHandPlay` override ในส่วน p23 รองรับ `returnGlass`, `omenCollapse`, `breakVessel`
- ปิด detail แล้ว return `game.p3dQueueChoice(...)` โดยไม่เรียก render หลัง queue สำเร็จ
- `p3dQueueChoice` เปลี่ยน pendingChoice แล้ว return true แต่ไม่วาด UI
- click handler ของ `data-play` เรียก beginHandPlay แล้ว return เช่นกัน
- เมื่อผู้เล่นเปิดคำใบ้จนเกิด full render หน้าต่าง choice จึงปรากฏ และปริศนา 2–3 สามารถแก้ผลจนชนะได้ นี่เป็น workaround ไม่ใช่ acceptance flow

จุดค้นหาใน index.html (เลขบรรทัดอาจเปลี่ยน):

- `const p23BeginHandBase=beginHandPlay;` / `type:'p23_prepare_play'` ประมาณ 38055–38066
- `Game.prototype.p3dQueueChoice` ประมาณ 35838
- `p3dDecorateChoiceUi` ประมาณ 36135 และ handler `data-p3d-choice`

ขอบเขตแก้ที่อนุญาต: การ refresh/render UI หลังตั้ง choice ใน owner ของ special hand play ข้างต้น ตรวจให้ render เพียงตามความจำเป็น รักษา return value, options, targetOwner, sourceUid และขั้นตอนจ่าย Cost เดิม ห้ามเปลี่ยนการเลือกเป้าหมาย กติกา combat, trigger, Cost, card data หรือเงื่อนไขชัยชนะเพื่อหลบอาการ

Acceptance P1:

- Omen of Collapse: กดเล่นแล้วหน้าต่างเลือกเป้าหมายแสดงทันทีโดยไม่ต้องกดคำใบ้หรือ action อื่น
- Return Through Glass: เลือกเป้าหมายที่ถูกต้องได้ รวมทั้ง Creature ศัตรูใน et3
- Break the Vessel: ตรวจ flow เลือกเป้าหมายใน owner เดียวกันด้วย เป็น regression check ไม่ใช่เพิ่มความสามารถ
- เลือกเป้าหมายแล้วเปิดการจ่าย Resonance ตามเดิม จ่ายเพียงครั้งเดียว; ไม่เรียก effect/trigger ซ้ำ
- ปริศนา et2 และ et3 ชนะได้ผ่าน UI ปกติแบบไม่ใช้คำใบ้
- et1 Equipment/RIFTSTRIKE และ et4 Combat/Journey/Claim ยังชนะได้
- ทดลอง desktop และ mobile landscape/touch; หากมี drag-to-play อยู่เดิม ให้ตรวจ entry point นั้นด้วย
- เมื่อยกเลิก payment ไม่เสียทรัพยากร และเริ่มใหม่/กลับแผนที่ไม่ทิ้ง pendingChoice ค้าง

## P2 — เซฟ version 1 ที่ข้อมูลไม่ครบทำให้ Adventure error

ผลกระทบ: JSON อ่านได้แต่ schema ไม่ครบ ทำให้หน้า Adventure ใช้งานไม่ได้

ใช้ browser profile ทดสอบแยกจากผู้ใช้ ตั้งค่า:

```js
localStorage.setItem('wonderbound_adventure_v1', JSON.stringify({version:1, completed:{}}));
```

เปิด Adventure → Basic: current working tree error `Cannot read properties of undefined (reading 'p1')`; baseline d7be81e error ลักษณะเดียวกันขณะอ่าน `beacon`

สาเหตุที่ยืนยัน: `load()` ตรวจเพียง version และ completed แล้วรับ object ทันที โดยไม่ตรวจ/default ฟิลด์ที่ UI ใช้ เช่น mastery, achievements และ owned; `initial()` มี defaults แต่ไม่ได้ใช้กับ object ที่ผ่าน validation แบบไม่ครบ

จุดค้นหา: `const STORE = 'wonderbound_adventure_v1'`, `const load = () =>`, `const initial = () =>` ประมาณ 40047

ขอบเขตแก้ที่อนุญาต: validation/normalization ของ Adventure progress ที่ load เท่านั้น ใช้ defaults ที่สอดคล้องกับ initial เดิม รักษาข้อมูลที่ถูกต้องของ completed, mastery, achievements, owned, echoes, puzzles และ tutorialCompleted อย่าล้าง progress ที่ใช้ได้ ห้ามลบ localStorage ผู้ใช้ ไม่เปลี่ยน storage key/version ไม่เพิ่มระบบ migration/economy ใหม่ และไม่ปรับรางวัลหรือ unlock rules

Acceptance P2:

- ไม่มีเซฟ, malformed JSON และ version ไม่รองรับ: fallback ปลอดภัยตามพฤติกรรมเดิม
- `{version:1,completed:{}}`: เปิด hub, Basic, Story และคู่มือได้โดยไม่ error
- ฟิลด์ที่จำเป็นเป็น null/array/string หรือขาด: normalize/fallback อย่างปลอดภัยตามเหตุผลที่บันทึกไว้
- valid v1 save ที่มี progress จริง: completed/mastery/achievements/owned/echoes/puzzles/tutorialCompleted ต้องคงค่าเดิม
- Partial save ที่มี completed และ puzzles ถูกต้องแต่ขาดฟิลด์อื่น: รักษาข้อมูลที่กู้ได้ ไม่รีเซ็ตทั้ง profile โดยไม่จำเป็น
- ชนะ p1: รับรางวัลครั้งแรกหนึ่งครั้ง ปลดล็อก p2 และ reload แล้วยังอยู่; เล่นซ้ำไม่แจกซ้ำ
- Progress ปริศนายังคงแยกจาก campaign rewards
- ทดสอบด้วย isolated profile ห้ามใช้/ลบเซฟใน browser ของผู้ใช้

## สิ่งที่ต้องคงไว้และขอบเขตไฟล์

- Living Atlas เป็นหน้าเลือกโหมด; Basic 6 บทเรียน + 4 ปริศนา = 10; Story = 14; Expedition ยัง disabled
- Tree คนละโหมด, stage IDs, setup, unlock dependencies, story text, existing rewards และ schema version เดิม
- Lore Next/Back/Skip และการกลับสู่ Tree ของด่านนั้น
- Tutorial snapshot ข้าม `wb-startup-loading-controller` ต่อไป; เกมหลักยังมี loading controller
- ภาพ Asset ทั้งหมด, artFocus, card data, AT/HP, abilities, AI, combat/turn/Journey/Claim ห้ามเปลี่ยน
- ไม่สร้าง Artwork เพิ่ม ไม่แก้ CSS/เลย์เอาต์เพื่อแก้ bug เหล่านี้
- Implementation delta ควรอยู่ใน `index.html` เท่านั้น อนุญาตเพิ่มรายงาน/patch ส่งกลับใน `docs/handoffs/` ไม่แก้เอกสาร canonical หรือไฟล์เกมอื่น

## Regression ที่ต้องตรวจหลังแก้

- Basic 10 nodes, Story 14 nodes, Expedition disabled; fresh/valid/partial save
- ปริศนาทั้ง 4 ชนะด้วย UI จริง, hint 3 ระดับ, restart คืนสนามเดิม, จบเทิร์นแล้วปริศนาแพ้
- เข้า/ออก Battle ของบทเรียนและแขนง Story รวมทั้ง convergence; คืน Tree ถูกโหมด
- คู่มือเปิด–ปิดเร็ว, Escape, spotlight, เดินครบ, finish เข้าด่านแรก และ portrait orientation gate
- Lore Next/Back/Skip; progress ไม่เปลี่ยนจาก navigation
- Normal Duel: mulligan, Attune, ACTION, AI turn; Deck Builder เปิด/filter/reset/back
- Desktop และ mobile landscape; console/pageerror/network ตรวจเฉพาะที่เป็นข้อผิดพลาดจริง
- ตรวจ syntax ของ inline scripts และ `git diff --check`
- เปรียบเทียบ stage/card/reward definitions กับ snapshot ก่อนแก้ ต้องไม่เปลี่ยน

ระบุผล PASS/FAIL/NOT TESTED ตามจริง ห้ามใช้การแก้ game.winner หรือเปลี่ยนข้อมูลเกมใน console เป็นหลักฐานว่าปริศนาชนะผ่าน UI ห้ามกล่าวว่า iOS/Safari หรือบอสทุกด่านผ่าน หากไม่ได้ทดสอบจริง

## หลักฐานจาก Codex

อยู่ในเครื่องเดียวกัน:

`C:\Users\Warunyu.N\.codex\visualizations\2026\10\05\01a10a2c-621b-7ee0-894b-55863a750b1c\adventure-regression\`

- `REGRESSION_REVIEW.md` — รายงานเต็ม พร้อมขอบเขตและข้อจำกัด
- `review.patch` — diff ของงาน Codex ก่อนส่ง bug-fix อย่านับเป็น delta ของคุณ
- `bug-omen-choice-missing.png`, `choice-bug-state.json` — P1
- `et3-choice-after-hint.png` — workaround ที่ยืนยัน root cause
- `incomplete-save-comparison.json` — P2 current/baseline
- ภาพ Atlas/Basic/Story หลายขนาดจอ และ `mobile-hand-expanded.png`

หากทำงานคนละเครื่องและไม่มีหลักฐาน local เหล่านี้ ให้ใช้ reproduction ในเอกสารนี้กับ repository ปัจจุบัน ห้ามถือว่าหลักฐานที่ไม่มีได้ผ่านตรวจแล้ว

## ส่งกลับให้ Codex — บังคับก่อน Dev

เมื่อแก้เสร็จ:

1. เก็บการแก้ไว้เป็น working-tree changes; ห้าม stage/commit/push
2. สร้าง `docs/handoffs/ANTIGRAVITY_ADVENTURE_BUGFIX_RETURN.md` ระบุ baseline ที่รับมา, root cause, owner, exact changes, PASS/FAIL/NOT TESTED, วิธี reproduce, screenshots/log paths, ข้อจำกัด และ git status
3. สร้าง `docs/handoffs/ANTIGRAVITY_ADVENTURE_BUGFIX_DELTA.patch` ที่มีเฉพาะ delta ของ Antigravity เทียบกับ snapshot ก่อนเริ่ม ไม่รวมงาน Codex ที่มีอยู่ก่อน และไม่รวมรูป/ข้อมูล canonical
4. แนบผลทดสอบ P1/P2 และ regression ที่ตรวจจริง หากยังไม่ผ่าน ให้หยุดและระบุ blocker ห้ามรายงาน complete
5. แจ้งผู้ใช้ด้วยข้อความพร้อมส่งกลับมายังแชต Codex: “Antigravity แก้ P1/P2 แล้ว กรุณาตรวจ docs/handoffs/ANTIGRAVITY_ADVENTURE_BUGFIX_RETURN.md และ delta patch ก่อนนำขึ้น Dev”
6. หยุดรอ Codex ตรวจ diff และทดสอบซ้ำ ไม่มีสิทธิ์นำเข้า Dev/Main เอง แม้การทดสอบของคุณผ่าน

หากมีช่องทางส่งข้อความกลับแชต Codex ที่ผู้ใช้อนุญาตไว้ ให้ใช้ช่องทางนั้นพร้อมอ้างอิงรายงาน ไม่อ้างว่าส่งแล้วหากยังไม่ได้ส่งจริง หากไม่มีช่องทาง ให้รายงานต่อผู้ใช้เพื่อส่งข้อความกลับแชตนี้

Codex จะตรวจเมื่อได้รับรายงานส่งกลับ การมีไฟล์ RETURN อย่างเดียวไม่เท่ากับ Codex อนุมัติให้ push
