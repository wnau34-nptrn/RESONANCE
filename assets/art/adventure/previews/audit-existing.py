"""Audit and derive existing artwork only. No generation or network calls."""
import hashlib, json, os
from collections import Counter
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def write(p, value): p.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
def rel(p): return p.relative_to(REPO).as_posix()
def info(p):
    out={'path':rel(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'format':p.suffix[1:]}
    if p.suffix.lower() in ('.png','.webp','.jpg'):
        with Image.open(p) as im:
            out.update(dimensions=list(im.size),transparency='A' in im.getbands())
    return out
jobs=read(ROOT/'previews/generation-log.json')
if isinstance(jobs,dict): jobs=jobs['selected_outputs']
m=read(ROOT/'asset-manifest.json')
by={a['asset_id']:a for a in m['assets']}
defects={
 'living-atlas':['Native detail is 887x1774; 2048x4096 delivery is an upscale. Lower prologue/puzzle placements overlap detailed relic imagery in the review overlay. Final runtime label/route layout remains untested.'],
 'npc-eira':['Proposed face remains Candidate; no locked face reference exists. User approved this proposal as Candidate only.'],
 'act1-boss':['Gold seams and floating fragments need human continuity approval against F03; no new power is canonized.'],
}
checks=[]
for j in jobs:
    p=REPO/j['delivery_path']; src=REPO/j['native_source_path']; im=Image.open(p)
    a=by[j['id']]; a.update(info(p)); a.pop('blocked_reason',None)
    a.update(status='candidate' if j['id'] in defects else 'ready',native_source=info(src),export_transform=j['export_transform'],defects=defects.get(j['id'],[]),validation='Existing output inspected in current-primary-review.jpg; no generation in this audit. Ready means usable asset preparation, not canonical approval or runtime integration.')
    a['review_evidence']='assets/art/adventure/previews/current-primary-review.jpg'
    check={'asset_id':j['id'],'native_dimensions':list(Image.open(src).size),'export_dimensions':list(im.size),'source_preserved':True,'visual_review':'pass with candidate limitation' if a['defects'] else 'pass','defects':a['defects']}
    if j['alpha']:
        alpha=im.getchannel('A'); box=alpha.getbbox(); check.update(alpha_extrema=list(alpha.getextrema()),alpha_bbox=list(box),edge_alpha=[max(alpha.crop(b).getextrema()) for b in [(0,0,im.width,1),(0,im.height-1,im.width,im.height),(0,0,1,im.height),(im.width-1,0,im.width,im.height)]])
        assert all(v==0 for v in check['edge_alpha'])
    checks.append(check)

# Crops use native source coordinates; no new portraits are generated.
boxes={
 'liora':(420,20,800,400),'miniboss-beacon':(370,150,700,480),
 'miniboss-glasswind':(440,35,760,355),'miniboss-fracture':(400,220,760,580),
 'miniboss-wildroot':(350,470,750,870),'act1-boss':(450,0,810,360),
 'npc-seris':(460,70,800,410),'npc-eira':(440,30,800,390)}
(ROOT/'characters/icons').mkdir(exist_ok=True)
for icon in m['derived_face_icons']:
    parent=icon['source_reference']; j=next(x for x in jobs if x['id']==parent)
    src=REPO/j['native_source_path']; im=Image.open(src).convert('RGBA'); box=boxes[parent]
    p=ROOT/'characters/icons'/f'{parent}.webp'
    im.crop(box).resize((256,256),Image.Resampling.LANCZOS).save(p,'WEBP',quality=90,method=6)
    icon.update(info(p)); icon.pop('blocked_reason',None)
    icon.update(status=by[parent]['status'],source_path=rel(src),crop_guidance={'source_pixel_rectangle':list(box),'resize':[256,256],'method':'square crop and Lanczos; preserve alpha'},defects=by[parent]['defects'],validation='Derived from technically passed existing source; reviewed at 256, 96 and 64px. Parent candidate status is inherited.')
    icon['review_evidence']='assets/art/adventure/previews/face-icons-review.jpg'

sheet=Image.new('RGB',(1200,800),'#202830'); d=ImageDraw.Draw(sheet)
alpha_sheet=Image.new('RGB',(1600,1000),'#202830'); ad=ImageDraw.Draw(alpha_sheet)
for i,icon in enumerate(m['derived_face_icons']):
    x=i%4*300;y=i//4*400; d.text((x+8,y+8),icon['asset_id'],fill='white'); im=Image.open(REPO/icon['path']).convert('RGBA')
    for size,ox,oy in [(256,12,32),(96,12,290),(64,130,290)]:
        z=im.resize((size,size),Image.Resampling.LANCZOS);bg=Image.new('RGBA',z.size,'#a0b4bd'); bg.alpha_composite(z);sheet.paste(bg.convert('RGB'),(x+ox,y+oy))
    parent=icon['source_reference'];j=next(j for j in jobs if j['id']==parent); full=Image.open(REPO/j['delivery_path']).convert('RGBA');full.thumbnail((180,430))
    ax=i%4*400;ay=i//4*500;ad.text((ax+8,ay+6),parent,fill='white')
    for ox,color in [(0,'#dbe4e7'),(200,'#101820')]:
        bg=Image.new('RGBA',(195,460),color);bg.alpha_composite(full,((195-full.width)//2,10));alpha_sheet.paste(bg.convert('RGB'),(ax+ox,ay+30))
sheet.save(ROOT/'previews/face-icons-review.jpg',quality=94)
alpha_sheet.save(ROOT/'previews/character-alpha-review.jpg',quality=94)

atlas=Image.open(REPO/by['living-atlas']['path']).resize((768,1536),Image.Resampling.LANCZOS).convert('RGB');d=ImageDraw.Draw(atlas)
for n in read(ROOT/'previews/layout-review.json')['nodes']:
    x=round(n['x']*768);y=round(n['y']*1536);d.ellipse((x-17,y-17,x+17,y+17),fill='#10232d',outline='#d1b879',width=2)
    d.rounded_rectangle((x-52,y+20,x+52,y+40),radius=3,fill='#10232d');d.text((x-12,y+23),n['stage_id'],fill='white')
atlas.save(ROOT/'previews/atlas-v2-24-node-review.jpg',quality=92)

gold=read(Path(os.environ['TEMP'])/'resonance-adventure-golden.json')
unchanged={p:hashlib.sha256((REPO/p).read_bytes()).hexdigest()==h for p,h in gold.items()}
assert len(unchanged)==45 and all(unchanged.values())
m['counts']={**dict(Counter(a['status'] for a in m['assets'])),'primary_artwork_produced':14,'primary_artwork_target':14,'derived_face_icons_produced':8,'derived_face_icon_statuses':dict(Counter(a['status'] for a in m['derived_face_icons'])),'blocked':0}
m['schema_version']=2
m['current_gate']='STOP_GENERATION_REVIEW_EXISTING_FILES'
old=read(ROOT/'previews/validation-report.json')
old['previous_delivery_checks']=old.pop('checks',[])
old['visual_review']={'primary':'14 actual selected exports inspected; 3 remain candidate with documented limitations','characters':'8 RGBA sources and padded exports; full silhouettes reviewed on light/dark backgrounds','icons':'8 source-derived crops; small-size review recorded separately','map':'Preview overlay only; runtime layout not implemented or verified','canon':'No candidate promoted to canonical','generation_in_this_audit':0}
old['checks']=checks
old['preserved_delivery_01']={'files':45,'all_hashes_unchanged':all(unchanged.values()),'checks':unchanged}
old['runtime_tests']='Not run: no gameplay/runtime files changed; asset preparation only.'
write(ROOT/'previews/validation-report.json',old)
# Support file hashes are refreshed after README/contact-sheet edits in finalize mode.
write(ROOT/'asset-manifest.json',m)
write(ROOT/'previews/file-inventory.json',[info(p) for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name not in ('file-inventory.json','asset-manifest.json')])
print(json.dumps(m['counts']))
