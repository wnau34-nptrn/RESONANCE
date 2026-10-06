"""Document existing production history and refresh metadata. Never generate."""
import json, hashlib
from pathlib import Path
from PIL import Image
R=Path(__file__).resolve().parents[1];REPO=R.parents[2]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
jobs=read(R/'previews/generation-log.json')
if isinstance(jobs,dict):jobs=jobs['selected_outputs']
gen=Path.home()/'.codex/generated_images/01a10f7b-5165-79d3-bd61-65cce8b5613b'
selected=['1d9ec95b-089a-4da9-9dac-8765fb828b7b','fa0fd1a5-8e8c-442c-b01f-142c2fe28b36','6b7f2bf7-2f36-4a8e-a019-ef3455dd1b2f','44276135-195c-4f4d-895f-2c2690e1551a','2aa89d76-bfa8-41f6-ad0d-949e38e2d193','3cf712c8-fcbd-4b03-b7fb-996e8e5ca996','4890e6b5-2ec4-41c7-8d24-42eb35334a60','0f1af8ed-beb0-4708-8ace-467ab6ec8cbe','4c149380-d49d-4be4-a429-77d8f7036e0f','e5c612a5-5683-4454-8151-69b2e6fcb38b','59f4033c-b167-4cbe-a18d-7acf5777460c','0206a8c2-99d8-4514-9c95-4b17da8a9efd','e60b7532-9ea1-4037-a116-4d20ef02fd96','4e9307ae-a8f1-4019-af24-bbabf0370a62']
rejected={
 'living-atlas':('312a2c7f-51e7-4958-ac92-dede6fcc5f01','Earlier style proof: overly dense central architecture; user requested quieter Atlas.'),
 'miniboss-glasswind':('978cd0dd-b31c-4ec4-b013-4fc675477c5d','Landscape/scenery persisted instead of isolated transparent portrait.'),
 'miniboss-fracture':('d604aafa-5f04-4f0e-9bb8-c375d1624add','Landscape/scenery persisted instead of isolated transparent portrait.'),
 'act1-boss':('00eee2ef-691d-4b4b-b48a-835212a5722f','Landscape/scenery persisted instead of isolated transparent portrait.'),
 'npc-seris':('f32b4b76-5d03-4303-b688-f120644fba2b','Landscape/scenery persisted instead of isolated transparent portrait.'),
 'npc-eira':('09bf3a57-8884-4483-96c0-9f4eda3ba93d','Skin tone did not match approved deep-brown proposal.'),
 'miniboss-wildroot':('34f485e2-54c5-47bf-b1ad-dc41e49d5db8','Canopy clipping in initial isolated output.')}
attempts=[]
for j,uuid in zip(jobs,selected):
    if j['id'] in rejected:
        old,reason=rejected[j['id']];p=gen/f'exec-{old}.png'
        record={'asset_id':j['id'],'attempt':1,'status':'candidate-superseded','selected':False,'defect':reason,'source_path':str(p),'references':next(a['source_reference'] for a in read(R/'asset-manifest.json')['assets'] if a['asset_id']==j['id']),'exact_prompt':None,'prompt_recovery_status':'Exact initial prompt not retained in repository; do not invent or regenerate it.','historical_note':'Preceded current no-retry gate; no per-asset correction approval is inferred.'}
        if p.exists():record.update(bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),native_dimensions=list(Image.open(p).size),source_available_at_audit=True)
        else:record['source_available_at_audit']=False
        attempts.append(record)
    src=REPO/j['native_source_path'];p=gen/f'exec-{uuid}.png'
    attempts.append({'asset_id':j['id'],'attempt':2 if j['id'] in rejected else 1,'status':'completed-reviewed','selected':True,'source_path':str(p),'repository_source_path':j['native_source_path'],'delivery_path':j['delivery_path'],'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'exact_prompt':j['prompt'],'references':j['refs'],'native_dimensions':j['native_dimensions'],'review_evidence':'assets/art/adventure/previews/current-primary-review.jpg','audit_verified_original_matches_repository':p.exists() and p.read_bytes()==src.read_bytes()})
write(R/'previews/generation-log.json',{'schema_version':2,'current_gate':'STOP_GENERATION_REVIEW_EXISTING_FILES','generation_calls_in_current_audit':0,'in_flight_requests':[],'request_start_metadata_gap':'Historical calls were not recorded before submission. This log is reconstructed from existing outputs and retained selected prompts, not fabricated request-start records.','generation_calls_historical':21,'historical_breakdown':'1 first Atlas proof + 14 selected outputs in continuation + 6 historical corrections; exports and 8 crops are not generations.','selected_outputs':jobs,'attempts':attempts})
(R/'README.md').write_text('''# Adventure asset preparation — inspected existing delivery

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
''',encoding='utf-8')
(R/'previews/index.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Adventure asset audit</title><style>body{background:#10202a;color:#edf1f3;font:16px system-ui;margin:24px}img{max-width:100%;height:auto}a{color:#9ddce0}.map{max-width:768px}</style><h1>Existing Adventure asset audit</h1><p>14 primary artworks: 11 ready, 3 candidate. Eight derived icons: 6 ready, 2 candidate. Generation stopped; no generation in this audit.</p><p><a href="../README.md">README</a> · <a href="../HANDOFF.md">Handoff</a> · <a href="../asset-manifest.json">Manifest</a> · <a href="validation-report.json">Validation</a></p><h2>Selected 14 artworks</h2><img src="current-primary-review.jpg" alt="14 actual artworks"><h2>Light and dark alpha review</h2><img src="character-alpha-review.jpg" alt="Eight isolated characters"><h2>Derived icons</h2><img src="face-icons-review.jpg" alt="Eight source-derived icons at 256, 96 and 64 pixels"><h2>Atlas candidate overlay</h2><img class="map" src="atlas-v2-24-node-review.jpg" alt="24 preview placements; lower detail remains a limitation"><h2>Preserved UI</h2><img src="ui-contact-sheet.jpg" alt="21 SVG assets"><h2>Preserved stages</h2><img src="stage-contact-sheet.jpg" alt="24 stage thumbnails"></html>''',encoding='utf-8')
# Refresh all support metadata after writing final documents, without touching handoff/policy.
m=read(R/'asset-manifest.json');primary={a['path'] for a in m['assets']}|{a['path'] for a in m['derived_face_icons']}
support=[]
for p in sorted(R.rglob('*')):
    if not p.is_file() or p.name in ('asset-manifest.json','file-inventory.json'):continue
    path=p.relative_to(REPO).as_posix(); rec={'path':path,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'format':p.suffix[1:]}
    if p.suffix.lower() in ('.png','.webp','.jpg'):
        im=Image.open(p);rec.update(dimensions=list(im.size),transparency='A' in im.getbands())
    if path not in primary:support.append({**rec,'purpose':'Source, reference, history or review evidence; not another generated asset'})
m['supporting_artifacts']=support;write(R/'asset-manifest.json',m)
write(R/'previews/file-inventory.json',{'scope':'Actual files; source/export/crop are distinguished in manifest','files':support+[{'path':a['path'],'sha256':a['sha256'],'dimensions':a['dimensions']} for a in m['assets']+m['derived_face_icons']]})
print('Documented attempts:',len(attempts),'selected original byte matches:',sum(a.get('audit_verified_original_matches_repository',False) for a in attempts))
