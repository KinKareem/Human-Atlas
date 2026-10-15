import json,re
M=json.load(open('meta.json')); meta=M['meta']
ORD={'First':1,'Second':2,'Third':3,'Fourth':4,'Fifth':5,'Sixth':6,'Seventh':7,'Eighth':8,'Ninth':9,'Tenth':10,'Eleventh':11,'Twelfth':12}
ROM=['','I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']
B={'Parietal_bone':('Tulang Parietal','Os parietale'),'Frontal_bone':('Tulang Frontal','Os frontale'),'Occipital_bone':('Tulang Oksipital','Os occipitale'),'Temporal_bone':('Tulang Temporal','Os temporale'),'Sphenoid_bone':('Tulang Sfenoid','Os sphenoidale'),'Ethmoid_bone':('Tulang Etmoid','Os ethmoidale'),'Sinus_of_frontal_bone':('Sinus Frontal','Sinus frontalis'),'Sinus_of_sphenoid_bone':('Sinus Sfenoid','Sinus sphenoidalis'),'Inferior_nasal_concha_bone':('Konka Nasal Inferior','Concha nasalis inferior'),'Lacrimal_bone':('Tulang Lakrimal','Os lacrimale'),'Nasal_bone':('Tulang Hidung','Os nasale'),'Maxilla':('Tulang Rahang Atas','Maxilla'),'Palatine_bone':('Tulang Palatinum','Os palatinum'),'Zygomatic_bone':('Tulang Pipi','Os zygomaticum'),'Vomer':('Tulang Vomer','Vomer'),'Mandible':('Rahang Bawah','Mandibula'),'Hyoid_bone':('Tulang Hioid','Os hyoideum'),'Malleus':('Maleus','Malleus'),'Incus':('Inkus','Incus'),'Stapes':('Stapes','Stapes'),
'Anterior_cells_of_ethmoid_bone':('Sel Etmoid Anterior','Cellulae ethmoidales anteriores'),'Middle_cells_of_ethmoid_bone':('Sel Etmoid Tengah','Cellulae ethmoidales mediae'),'Posterior_cells_of_ethmoid_bone':('Sel Etmoid Posterior','Cellulae ethmoidales posteriores'),
'Thyroid_cartilage':('Tulang Rawan Tiroid','Cartilago thyroidea'),'Cricoid_cartilage':('Tulang Rawan Krikoid','Cartilago cricoidea'),'Arytenoid_cartilage':('Tulang Rawan Aritenoid','Cartilago arytenoidea'),'Corniculate_cartilage':('Tulang Rawan Kornikulata','Cartilago corniculata'),'Major_alar_cartilage':('Tulang Rawan Alar Mayor','Cartilago alaris major'),'Lateral_process_of_nasal_septal_cartilage':('Prosesus Lateral Tulang Rawan Septum Nasi','Processus lateralis cartilaginis septi nasi'),'Nasal_septal_cartilage':('Tulang Rawan Septum Nasi','Cartilago septi nasi'),
'Clavicle':('Tulang Selangka','Clavicula'),'Scapula':('Tulang Belikat','Scapula'),'Humerus':('Tulang Lengan Atas','Humerus'),'Radius':('Tulang Pengumpil','Radius'),'Ulna':('Tulang Hasta','Ulna'),'Hip_bone':('Tulang Panggul','Os coxae'),'Femur':('Tulang Paha','Femur'),'Patella':('Tempurung Lutut','Patella'),'Tibia':('Tulang Kering','Tibia'),'Fibula':('Tulang Betis','Fibula'),'Talus':('Tulang Talus','Talus'),'Calcaneus':('Tulang Tumit','Calcaneus'),'Navicular_bone':('Tulang Navikular','Os naviculare'),'Cuboid_bone':('Tulang Kuboid','Os cuboideum'),'Medial_cuneiform_bone':('Kuneiformis Medial','Os cuneiforme mediale'),'Intermediate_cuneiform_bone':('Kuneiformis Intermedial','Os cuneiforme intermedium'),'Lateral_cuneiform_bone':('Kuneiformis Lateral','Os cuneiforme laterale'),'Sesamoid_bones_of_foot':('Tulang Sesamoid Kaki','Ossa sesamoidea pedis'),
'Capitate_bone':('Tulang Kapitatum','Os capitatum'),'Hamate_bone':('Tulang Hamatum','Os hamatum'),'Lunate_bone':('Tulang Lunatum','Os lunatum'),'Pisiform_bone':('Tulang Pisiformis','Os pisiforme'),'Scaphoid_bone':('Tulang Skafoid','Os scaphoideum'),'Trapezium_bone':('Tulang Trapezium','Os trapezium'),'Trapezoid_bone':('Tulang Trapezoid','Os trapezoideum'),'Triquetrum_bone':('Tulang Triketrum','Os triquetrum'),
'Sacrum':('Tulang Sakrum','Os sacrum'),'Coccyx':('Tulang Ekor','Os coccygis'),'Atlas_(C1)':('Atlas (C1)','Atlas'),'Axis_(C2)':('Aksis (C2)','Axis'),'Manubrium_of_sternum':('Manubrium Sterni','Manubrium sterni'),'Body_of_sternum':('Korpus Sterni','Corpus sterni'),'Xiphoid_process':('Prosesus Xifoideus','Processus xiphoideus')}
R=['Tengkorak & Wajah','Gigi & Tulang Rawan Kepala-Leher','Tulang Belakang','Toraks','Ekstremitas Atas','Ekstremitas Bawah']
def info(b):
    d=None
    if b in B: i,l=B[b]
    elif (m:=re.match(r'^([A-Z][a-z]+)_rib$',b)): n=ORD[m[1]];i,l=f'Tulang Rusuk ke-{n}',f'Costa {ROM[n]}'
    elif (m:=re.match(r'^Costal_cartilage_of_(\w+)_rib$',b)): n=ORD[m[1].capitalize()];i,l=f'Tulang Rawan Kosta ke-{n}',f'Cartilago costalis {ROM[n]}'
    elif (m:=re.match(r'^Vertebra_([CTL])(\d+)$',b)):
        k,n=m[1],int(m[2]);nm={'C':('Servikal','cervicalis'),'T':('Torakal','thoracica'),'L':('Lumbal','lumbalis')}[k]
        i,l=f'Vertebra {nm[0]} {n}',f'Vertebra {nm[1]} {ROM[n]}'
    elif (m:=re.match(r'^(\w+)_metacarpal_bone$',b)): n=ORD[m[1]];i,l=f'Tulang Metakarpal ke-{n}',f'Os metacarpale {ROM[n]}'
    elif (m:=re.match(r'^(\w+)_metatarsal_bone$',b)): n=ORD[m[1]];i,l=f'Tulang Metatarsal ke-{n}',f'Os metatarsale {ROM[n]}'
    elif (m:=re.match(r'^(Proximal|Middle|Distal)_phalanx_of_(\w+)_finger_of_(hand|foot)$',b)):
        t={'Proximal':('Proksimal','proximalis'),'Middle':('Tengah','media'),'Distal':('Distal','distalis')}[m[1]];n=ORD[m[2].capitalize()];h=m[3]=='hand'
        i,l=f'Falang {t[0]} Jari {n} {"Tangan" if h else "Kaki"}',f'Phalanx {t[1]} digiti {ROM[n]} {"manus" if h else "pedis"}'
    else:
        m=re.match(r'^(Upper|Lower)_(\w+?)(_tooth)?$',b);w={'medial_incisor':'Seri Tengah','lateral_incisor':'Seri Samping','canine':'Taring','first_premolar':'Geraham Kecil 1','second_premolar':'Geraham Kecil 2','first_molar':'Geraham 1','second_molar':'Geraham 2'}[m[2]]
        i,l=f'Gigi {w} {"Atas" if m[1]=="Upper" else "Bawah"}',f'Dens {m[2].replace("_"," ")} {"maxillaris" if m[1]=="Upper" else "mandibularis"}'
    if re.match(r'^(Parietal|Frontal|Occipital|Temporal|Sphenoid|Ethmoid)_bone$',b): d='cranium'
    elif b=='Mandible': d='mandibula'
    elif b.startswith('Vertebra_') or b.startswith('Atlas') or b.startswith('Axis'): d='vertebra'
    elif 'sternum' in b: d='sternum'
    elif re.match(r'^[A-Z][a-z]+_rib$',b): d='kosta'
    else: d={'Clavicle':'klavikula','Scapula':'skapula','Humerus':'humerus','Radius':'radius','Ulna':'ulna','Hip_bone':'pelvis','Femur':'femur','Patella':'patela','Tibia':'tibia','Fibula':'fibula'}.get(b)
    # region
    if re.search(r'tooth|incisor|canine|premolar|cartilage',b) and not re.search(r'Costal',b): rg=1
    elif re.match(r'^(Vertebra|Atlas|Axis|Sacrum|Coccyx)',b): rg=2
    elif re.search(r'rib$|sternum|Xiphoid|Costal',b): rg=3
    elif re.search(r'Clavicle|Scapula|Humerus|Radius|Ulna|metacarpal|of_hand|Capitate|Hamate|Lunate|Pisiform|Scaphoid|Trapez|Triquetrum',b): rg=4
    elif re.search(r'Hip_bone|Femur|Patella|Tibia|Fibula|Talus|Calcaneus|Navicular|Cuboid|cuneiform|metatarsal|of_foot',b): rg=5
    else: rg=0
    # sort key
    if m:=re.match(r'^Vertebra_([CTL])(\d+)$',b): key='b%02d%02d'%('CTL'.index(m[1]),int(m[2]))
    elif b.startswith('Atlas'): key='a0'
    elif b.startswith('Axis'): key='a1'
    elif b=='Sacrum': key='c'
    elif b=='Coccyx': key='d'
    elif b=='Manubrium_of_sternum': key='a0'
    elif b=='Body_of_sternum': key='a1'
    elif b=='Xiphoid_process': key='a2'
    elif re.match(r'^[A-Z][a-z]+_rib$',b): key='r%02d'%ORD[b.split('_')[0]]
    elif b.startswith('Costal'): key='s%02d'%ORD[b.split('_')[3].capitalize()]
    else: key='z'+i
    return i,l,rg,key,d
items={}
for idx,(n,*_) in enumerate(meta):
    b=re.sub(r'\.(r|l)$','',n);s=n[len(b)+1:] if n!=b else ''
    it=items.setdefault(b,{'p':[],'s':set()});it['p'].append(idx);it['s'].add(s)
G=[[] for _ in R]
for b,it in items.items():
    i,l,rg,key,d=info(b);en=b.replace('_',' ')
    s=it['s'];side='kanan & kiri' if s=={'r','l'} else 'kanan' if s=={'r'} else 'kiri' if s=={'l'} else 'garis tengah'
    o={'id':b,'id_':i,'la':l,'en':en,'reg':R[rg],'side':side,'p':it['p']}
    if d: o['d']=d
    G[rg].append((key,o))
SKG=[{'g':R[k],'items':[o for _,o in sorted(G[k],key=lambda x:x[0])]} for k in range(len(R))]
print([ (g['g'],len(g['items'])) for g in SKG])
h=open('/mnt/user-data/outputs/anatomi-rangka.html',encoding='utf8').read()
def rep(a,b):
    global h
    assert h.count(a)==1,a; h=h.replace(a,b)
data='<script>const SK="%s";const SKM=%s;const SKG=%s;</script>\n'%(open('blob.b64').read(),json.dumps({'mn':M['mn'],'sc':M['sc'],'meta':meta},separators=(',',':')),json.dumps(SKG,ensure_ascii=False,separators=(',',':')))
rep('<script>\n// ===== DATA =====',data+'<script>\n// ===== DATA =====')
rep('PerspectiveCamera(40,1,.1,200)','PerspectiveCamera(40,1,.01,200)')
rep("function resetCam(){cam.position.set(dist*.35,dist*.25,dist*.9);ctl.target.set(0,0,0);ctl.update()}","function resetCam(){ctl.target.copy(tgt);cam.position.set(tgt.x+dist*.35,tgt.y+dist*.25,tgt.z+dist*.9);ctl.update()}")
rep("function show(k){mat=MATS[curLayer];","function show(k){mat=MATS[curLayer];skel.visible=false;tgt.set(0,0,0);")
rep("function build(f=''){","function buildProc(f=''){")
rep("function pick(id){","function pickProc(id){")
rep("build();pick(D[0].items[0].id)});","build();pick(curLayer==='rangka'?'__all':D[0].items[0].id)});")
rep("build();pick('cranium');","build();pick('__all');")
js=r'''
const tgt=new THREE.Vector3(),skel=new THREE.Group(),SKMESH=[];
(function(){
 const b=atob(SK),u=new Uint8Array(b.length);for(let i=0;i<b.length;i++)u[i]=b.charCodeAt(i);
 const w=new Uint16Array(u.buffer),mn=SKM.mn,sc=SKM.sc;
 SKM.meta.forEach(m=>{const nv=m[1],nf=m[2],vo=m[3],fo=m[4],p=new Float32Array(nv*3);
  for(let i=0;i<nv*3;i++)p[i]=mn[i%3]+w[vo+i]/65535*sc;
  const g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.BufferAttribute(p,3));
  g.setIndex(new THREE.BufferAttribute(w.slice(fo,fo+nf*3),1));g.computeVertexNormals();
  const n=m[0],c=/cartilage/.test(n)?0xa9c7cc:/tooth|incisor|canine|premolar/.test(n)?0xf5f2e8:0xe6dbc0;
  const me=new THREE.Mesh(g,new THREE.MeshStandardMaterial({color:c,roughness:.6}));skel.add(me);SKMESH.push(me)});
 scene.add(skel);
})();
function skFocus(l){const bx=new THREE.Box3();(l||SKMESH).forEach(m=>bx.expandByObject(m));const c=bx.getCenter(new THREE.Vector3()),r=bx.getSize(new THREE.Vector3()).length()/2;tgt.copy(c);dist=r*2.4;ctl.minDistance=r*.4;ctl.maxDistance=r*8;resetCam()}
const NOTE='<div class="note">Model 3D: BodyParts3D © DBCLS (CC BY-SA) melalui Z-Anatomy (CC BY-SA 4.0), disederhanakan untuk web. Konten edukasi, bukan pengganti rujukan medis.</div>';
function build(f=''){curLayer==='rangka'?buildSk(f):buildProc(f)}
function pick(id){curLayer==='rangka'?pickSk(id):pickProc(id)}
function buildSk(f){list.innerHTML='';
 const mk=o=>{const b=document.createElement('button');b.className='it';b.dataset.id=o.id;b.innerHTML=`${o.id_}<i>${o.la}</i>`;b.onclick=()=>pick(o.id);list.appendChild(b)};
 if(!f)mk({id:'__all',id_:'🧍 Seluruh rangka',la:'Systema skeletale'});
 SKG.forEach(g=>{const its=g.items.filter(o=>(o.id_+o.la+o.en).toLowerCase().includes(f));if(!its.length)return;const h=document.createElement('div');h.className='grp';h.textContent=g.g+' ('+its.length+')';list.appendChild(h);its.forEach(mk)});
 if(cur_id)mark()}
function pickSk(id){cur_id=id;mark();if(cur){scene.remove(cur);cur=null}skel.visible=true;
 const it=id==='__all'?null:SKG.flatMap(g=>g.items).find(o=>o.id===id),sel=it?new Set(it.p):null;
 SKMESH.forEach((m,i)=>{const mm=m.material,on=!sel||sel.has(i);mm.transparent=!on;mm.opacity=on?1:.12;mm.depthWrite=on;mm.emissive.setHex(sel&&on?0x7a2e10:0)});
 skFocus(it?it.p.map(i=>SKMESH[i]):null);
 if(!it){info.innerHTML=`<h2>Seluruh Rangka Manusia</h2><div class="sub"><i>Systema skeletale</i> · Human skeleton</div><div class="tags"><span>${SKMESH.length} struktur tulang dan tulang rawan</span></div><div class="grid"><div class="card"><h3>Cara memakai</h3><p>Pilih nama tulang di sidebar untuk menyorotnya di dalam rangka. Seret untuk memutar, scroll atau cubit untuk zoom, klik kanan untuk menggeser.</p></div></div>${NOTE}`;info.scrollTop=0;return}
 const d=it.d?D_rangka.flatMap(g=>g.items).find(x=>x.id===it.d):null;
 let h=`<h2>${it.id_}</h2><div class="sub"><i>${it.la}</i> · ${it.en}</div><div class="tags"><span>${it.reg}</span><span>Sisi: ${it.side}</span></div>`;
 if(d){const own=d.la.toLowerCase()===it.la.toLowerCase()||d.id==='mandibula';
  h+=`<div class="grid"><div class="card"><h3>Deskripsi</h3><p>${d.desc}</p></div><div class="card"><h3>Fungsi</h3><p>${d.fn}</p></div><div class="card"><h3>Hubungan</h3><p><b>Persarafan:</b> ${d.nerve}</p><p><b>Suplai darah:</b> ${d.blood}</p><p><b>Struktur terkait:</b> ${d.rel}</p></div><div class="card"><h3>Korelasi klinis</h3><p>${d.clin}</p></div></div>`+(own?'':`<div class="note">Penjelasan di atas bersifat umum untuk kelompok "${d.id_}", bukan khusus ${it.id_}.</div>`)}
 else h+=`<div class="grid"><div class="card"><h3>Lokasi</h3><p>Bagian dari ${it.reg}.</p></div><div class="card"><h3>Keterangan</h3><p>Deskripsi, persarafan, suplai darah, dan korelasi klinis untuk struktur ini belum ditulis.</p></div></div>`;
 info.innerHTML=h+NOTE;info.scrollTop=0}
'''
rep('// ===== UI =====',js+'\n// ===== UI =====')
open('/mnt/user-data/outputs/anatomi-rangka.html','w',encoding='utf8').write(h)
print(len(h)/1e6,'MB')
