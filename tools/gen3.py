import json,re,collections,cls,detail
from bones import B as BB
P='/mnt/user-data/outputs/anatomi-rangka.html'
N='Pleksus pulmonalis: parasimpatis dari n. vagus (X), simpatis dari trunkus simpatikus T1–T4.'
BL_='A. pulmonalis (darah kurang oksigen), v. pulmonalis (darah kaya oksigen), a. bronkialis (nutrisi paru).'
K=detail.K
def D(*a): return dict(zip(K,a))
DET={
'lobe_ra':D('Lobus atas paru kanan, di atas fisura horizontal dan oblik; mengandung segmen apikal, posterior, dan anterior.','Pertukaran gas: oksigenasi darah dan pelepasan CO₂.',N,BL_,'Trakea dan bronkus utama kanan, pleura, lobus tengah, apeks paru di pangkal leher, a. dan v. subklavia.','Tuberkulosis apikal, tumor Pancoast (sindrom Horner), pneumonia lobaris.'),
'lobe_rm':D('Lobus tengah paru kanan yang kecil berbentuk baji, di antara fisura horizontal dan oblik; segmen lateral dan medial.','Pertukaran gas.',N,BL_,'Atrium kanan jantung, lobus atas dan bawah kanan, diafragma, pleura.','Sindrom lobus tengah (atelektasis karena bronkus sempit tertekan), pneumonia lobaris.'),
'lobe_ri':D('Lobus bawah paru kanan, lobus terbesar paru kanan; segmen superior dan lima segmen basal.','Pertukaran gas; terutama berperan pada ventilasi saat posisi berdiri.',N,BL_,'Diafragma, hati (di bawah), lobus tengah dan atas, pleura.','Pneumonia aspirasi, abses paru, efusi pleura (cairan terkumpul di basal).'),
'lobe_ls':D('Lobus atas paru kiri, termasuk lingula yang setara lobus tengah kanan; segmen apikoposterior, anterior, lingular superior dan inferior.','Pertukaran gas.',N,BL_,'Jantung (insisura kardiaka), arkus aorta, a. subklavia kiri, pleura.','Tuberkulosis, tumor paru, pneumonia lingula.'),
'lobe_li':D('Lobus bawah paru kiri; segmen superior dan basal (anteromedial, lateral, posterior).','Pertukaran gas.',N,BL_,'Diafragma, lambung dan limpa (di bawah), lobus atas kiri, pleura.','Pneumonia lobus bawah, bronkiektasis, efusi pleura.'),
'trachea':D('Pipa fibrokartilago sekitar 10–12 cm dengan 16–20 cincin tulang rawan berbentuk C terbuka ke belakang; dari tulang rawan krikoid (C6) sampai karina (T4–T5).','Menyalurkan udara ke dan dari paru; mukosa bersilia membersihkan partikel (eskalator mukosiliar).','N. vagus (X) dan n. laringeus rekuren (parasimpatis), trunkus simpatikus.','Cabang a. tiroidea inferior dan a. bronkialis.','Laring (atas), esofagus (belakang), kelenjar tiroid, arkus aorta, bronkus utama (bifurkasi di karina).','Intubasi dan trakeostomi, stenosis trakea, aspirasi benda asing, kompresi oleh goiter.'),
'bronchus_main':D('Cabang pertama trakea di karina; bronkus kanan lebih pendek, lebar, dan vertikal dibanding kiri. Bronkus intermedius adalah lanjutan bronkus utama kanan setelah cabang lobus atas.','Menyalurkan udara ke tiap paru.',N,'A. bronkialis (cabang aorta toraks), v. bronkialis.','Trakea, a. dan v. pulmonalis (hilus), arkus aorta (kiri), v. azigos (kanan).','Benda asing lebih sering masuk bronkus kanan, karsinoma bronkogenik, bronkoskopi.'),
'bronchus_lobar':D('Cabang bronkus utama menuju tiap lobus (3 di kanan, 2 di kiri).','Menyalurkan udara ke satu lobus paru.',N,'A. bronkialis.','Bronkus utama, bronkus segmental, a. pulmonalis lobar.','Obstruksi menyebabkan atelektasis lobar, tumor endobronkial.'),
'bronchus_segmental':D('Bronkus tersier yang memasok satu segmen bronkopulmonal (10 di kanan, 8–10 di kiri); tiap segmen punya arteri sendiri dan dipisah septum jaringan ikat.','Menyalurkan udara ke satu segmen paru.',N,'A. bronkialis, cabang segmental a. pulmonalis.','Bronkus lobaris, bronkiolus, cabang a. pulmonalis segmental.','Segmentektomi, aspirasi (segmen posterior lobus atas dan superior lobus bawah saat telentang), bronkiektasis.'),
'epiglottis':D('Tulang rawan elastis berbentuk daun di belakang pangkal lidah, di atas pintu masuk laring.','Menutup aditus laringis saat menelan agar makanan tidak masuk jalan napas.','N. laringeus superior (ramus internus, cabang X); sensasi valekula dari n. glosofaringeus (IX).','A. laringea superior (cabang a. tiroidea superior).','Hioid (ligamen hioepiglotik), pangkal lidah, valekula, tulang rawan tiroid.','Epiglotitis (darurat jalan napas), aspirasi.'),
'nasopharynx':D('Bagian atas faring di belakang rongga hidung dan di atas palatum molle; mengandung muara tuba Eustachius dan tonsil faringeal (adenoid).','Jalur udara dari hidung ke orofaring dan penyeimbang tekanan telinga tengah.','Pleksus faringeal (IX dan X); sensasi dari n. maksilaris (V2).','A. faringea asendens, a. palatina asendens, cabang a. maksilaris.','Koana, tuba auditiva, atap sfenoid, orofaring, palatum molle.','Adenoid hipertrofi, otitis media, karsinoma nasofaring.'),
'oropharynx':D('Bagian tengah faring dari palatum molle sampai tepi atas epiglotis; tempat tonsil palatina dan tonsil lingual.','Jalur bersama udara dan makanan.','N. glosofaringeus (IX) untuk sensasi dan refleks muntah; n. vagus (X) untuk motorik.','A. tonsilaris, a. faringea asendens, a. lingualis dorsalis.','Rongga mulut (isthmus fausium), nasofaring, laringofaring, tonsil palatina.','Tonsilitis, abses peritonsilar, karsinoma orofaring.'),
'laryngopharynx':D('Bagian bawah faring dari tepi atas epiglotis sampai tulang rawan krikoid, menyempit menjadi esofagus; memiliki resesus piriformis.','Jalur menelan; makanan lewat di kanan dan kiri laring.','N. laringeus rekuren dan superior (X), pleksus faringeal.','A. tiroidea superior dan inferior, a. faringea asendens.','Laring (depan), esofagus (bawah), otot konstriktor faring.','Benda asing tersangkut di resesus piriformis, karsinoma hipofaring.'),
'nasal_mucosa':D('Lapisan mukosa rongga hidung: epitel respirasi bersilia, dan epitel olfaktorius di atap.','Menghangatkan, melembabkan, menyaring udara, dan mendeteksi bau.','N. olfaktorius (I) untuk bau; n. trigeminus (V1, V2) untuk sensasi.','A. sfenopalatina, a. etmoidalis anterior dan posterior, a. labialis superior (pleksus Kiesselbach).','Konka nasalis, septum nasi, sinus paranasal, koana.','Epistaksis, rinitis alergi, polip nasal.'),
'pleura':D('Selaput serosa dua lapis (pleura parietal dan viseral) yang membungkus paru, dengan rongga pleura berisi cairan tipis.','Mengurangi gesekan saat bernapas dan menjaga tekanan negatif rongga pleura agar paru mengembang.','Parietal: n. interkostalis dan n. frenikus (peka nyeri); viseral: pleksus pulmonalis (tidak peka nyeri).','Parietal: a. interkostalis dan a. torakika interna; viseral: a. bronkialis dan a. pulmonalis.','Paru, dinding dada, diafragma, mediastinum.','Pneumotoraks, efusi pleura, empiema, pleuritis, hemotoraks.'),
'diaphragm':D('Otot berbentuk kubah yang memisahkan rongga toraks dan abdomen; bagian sternal, kostal, dan lumbal, dengan hiatus untuk aorta, esofagus, dan v. kava inferior.','Otot utama inspirasi: berkontraksi mendatar sehingga volume toraks bertambah.','N. frenikus (C3–C5); n. interkostalis bawah untuk sensasi tepi.','A. frenika superior dan inferior, a. perikardiakofrenika, a. muskulofrenika.','Paru dan pleura (atas), hati, lambung, limpa (bawah), rusuk 7–12, vertebra L1–L3.','Hernia hiatus, hernia diafragmatika kongenital, paresis diafragma (cedera n. frenikus), cegukan.')}
GEN={'bronchus_main','bronchus_lobar','bronchus_segmental','larynx_cart','nasal_cart'}
LOBE={'Superior_lobe_of_right_lung':('Lobus Atas Paru Kanan','Lobus superior pulmonis dextri','lobe_ra',0),'Middle_lobe_of_right_lung':('Lobus Tengah Paru Kanan','Lobus medius pulmonis dextri','lobe_rm',1),'Inferior_lobe_of_right_lung':('Lobus Bawah Paru Kanan','Lobus inferior pulmonis dextri','lobe_ri',2),'Superior_lobe_of_left_lung':('Lobus Atas Paru Kiri','Lobus superior pulmonis sinistri','lobe_ls',3),'Inferior_lobe_of_left_lung':('Lobus Bawah Paru Kiri','Lobus inferior pulmonis sinistri','lobe_li',4)}
NAME={'Trachea':('Trakea','Trachea'),'Epiglottis':('Epiglotis','Epiglottis'),'Right_main_bronchus':('Bronkus Utama Kanan','Bronchus principalis dexter'),'Left_main_bronchus':('Bronkus Utama Kiri','Bronchus principalis sinister'),'Intermediate_bronchus':('Bronkus Intermedius','Bronchus intermedius'),'Right_superior_lobar_bronchus':('Bronkus Lobaris Atas Kanan','Bronchus lobaris superior dexter'),'Middle_lobar_bronchus':('Bronkus Lobaris Tengah','Bronchus lobaris medius'),'Right_inferior_lobar_bronchus':('Bronkus Lobaris Bawah Kanan','Bronchus lobaris inferior dexter'),'Left_superior_lobar_bronchus':('Bronkus Lobaris Atas Kiri','Bronchus lobaris superior sinister'),'Left_inferior_lobar_bronchus':('Bronkus Lobaris Bawah Kiri','Bronchus lobaris inferior sinister'),'Pleura':('Pleura','Pleura'),'Oropharynx':('Orofaring','Pars oralis pharyngis'),'Nasopharynx':('Nasofaring','Pars nasalis pharyngis'),'Laryngopharynx':('Laringofaring','Pars laryngea pharyngis'),'Mucosa_of_nasal_cavity':('Mukosa Rongga Hidung','Tunica mucosa nasi'),'Diaphragm':('Diafragma','Diaphragma')}
ADJ={'apical':('Apikal','apicalis'),'posterior':('Posterior','posterior'),'anterior':('Anterior','anterior'),'lateral':('Lateral','lateralis'),'medial':('Medial','medialis'),'superior':('Superior','superior'),'inferior':('Inferior','inferior'),'apicoposterior':('Apikoposterior','apicoposterior'),'lingular':('Lingular','lingularis'),'basal':('Basal','basalis'),'anteromedial':('Anteromedial','anteromedialis')}
GN=['Paru-paru','Saluran Napas Bawah','Saluran Napas Atas','Selaput & Otot Pernapasan']
meta=json.load(open('meta_organ.json'))['meta']
its=collections.OrderedDict()
for i,m in enumerate(meta):
    b,s,side,t=cls.split(m[0]); it=its.setdefault(b,{'p':[],'s':set()}); it['p'].append(i)
    sd=side or ('r' if re.search('right',b,re.I) else 'l' if re.search('left',b,re.I) else '')
    if sd: it['s'].add(sd)
def sidestr(s): return 'kanan & kiri' if s=={'r','l'} else 'kanan' if s=={'r'} else 'kiri' if s=={'l'} else 'garis tengah'
G=[[] for _ in GN]
for b,it in its.items():
    d=None;gen=0;key='z'
    if b in LOBE: n,l,d,k=LOBE[b];g=0;key='a%d'%k
    elif b=='Trachea': n,l=NAME[b];g=1;d='trachea';key='a'
    elif (m:=re.match(r'^\(?([A-Za-z_]+?)_segmental_bronchus_of_(right|left)_lung\)?(?:_\((.+)\))?$',b)):
        w=m[1].lower().split('_'); w=w[::-1] if ('lingular' in w or 'basal' in w) else w
        n='Bronkus Segmental '+' '.join(ADJ[x][0] for x in w)+(' (B'+m[3].replace('B','')+')' if m[3] else '')+' Paru '+('Kanan' if m[2]=='right' else 'Kiri')
        l='Bronchus segmentalis '+' '.join(ADJ[x][1] for x in w)+' pulmonis '+('dextri' if m[2]=='right' else 'sinistri'); g=1;d='bronchus_segmental';gen=1;key='d'+n
    elif b in NAME:
        n,l=NAME[b]
        if 'main' in b or 'Intermediate' in b: g=1;d='bronchus_main';gen=1;key='b'+n
        elif 'lobar' in b: g=1;d='bronchus_lobar';gen=1;key='c'+n
        elif b in('Pleura','Diaphragm'): g=3;d=b.lower().replace('diaphragm','diaphragm');key=b
        else: g=2;d={'Epiglottis':'epiglottis','Oropharynx':'oropharynx','Nasopharynx':'nasopharynx','Laryngopharynx':'laryngopharynx','Mucosa_of_nasal_cavity':'nasal_mucosa'}[b];key='z'+n
    else:
        n,l=BB[b];g=2;d=detail.dkey(b);gen=1;key='y'+n
    o={'id':b,'n':n,'l':l,'e':b.replace('_',' '),'r':GN[g],'s':sidestr(it['s']),'p':it['p']}
    if d: o['d']=d
    if gen: o['g']=1
    G[g].append((key,o))
groups=[{'g':GN[i],'items':[o for _,o in sorted(G[i],key=lambda x:x[0])]} for i in range(4)]
print([(g['g'],len(g['items'])) for g in groups])
for g in groups:
    for o in g['items']:
        if o.get('d') and o['d'] not in DET and o['d'] not in detail.R: print('NO DET',o['id'],o['d'])
M=json.load(open('meta_organ.json'))
dj=lambda x:json.dumps(x,ensure_ascii=False,separators=(',',':'))
h=open(P,encoding='utf8').read()
def rep(a,b):
    global h
    assert h.count(a)==1,(h.count(a),a); h=h.replace(a,b)
rep('};const DET=',',organ:{b:"%s",m:%s,g:%s}};const DET='%(open('blob_organ.b64').read(),dj(M),dj(groups)))
rep('</script>\n<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js',';Object.assign(DET,%s);</script>\n<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js'%dj(DET))
rep('#tabs button{flex:1;padding:7px 4px;','#tabs button{flex:1;padding:7px 2px;')
rep('#q{margin:0 12px 8px;','#sys{display:none;flex-wrap:wrap;gap:4px;margin:0 12px 8px}\n#sys button{padding:4px 8px;border:1px solid var(--line);border-radius:99px;background:var(--soft);color:var(--txt);font-size:11px;cursor:pointer}\n#sys button.on{background:var(--acc);color:#fff;border-color:var(--acc)}\n#sys button:disabled{opacity:.45;cursor:not-allowed}\n#q{margin:0 12px 8px;')
rep('<button data-l="saraf">⚡ Saraf</button></div>','<button data-l="saraf">⚡ Saraf</button><button data-l="organ">🫁 Organ</button></div>\n  <div id="sys"><button class="on">Pernapasan</button><button disabled title="Segera hadir">Pencernaan</button><button disabled title="Segera hadir">Peredaran darah</button><button disabled title="Segera hadir">Urinari</button><button disabled title="Segera hadir">Reproduksi</button><button disabled title="Segera hadir">Endokrin</button></div>')
rep("const n=m[0],c=k!=='rangka'?COL[k]:","const n=m[0],c=k==='organ'?ocol(n):k!=='rangka'?COL[k]:")
rep("side:k==='saraf'?2:0","side:k==='saraf'||k==='organ'?2:0")
rep("me.userData.side=sm?sm[1]:'';","me.userData.side=sm?sm[1]:/right/i.test(n)?'r':/left/i.test(n)?'l':'';if(k==='organ'&&/Pleura|Mucosa/.test(n))me.userData.gh=.28;")
rep('saraf:0x7a5c00}','saraf:0x7a5c00,organ:0x7a3030}')
rep('// ===== model =====',"function ocol(n){return /lobe_of/.test(n)?0xe59a9a:/bronch|Trachea/.test(n)?0x9fb7d9:/Pleura|Mucosa/.test(n)?0xf0cdbd:/Diaphragm/.test(n)?0xb04a3c:/cartilage|Epiglottis/.test(n)?0xa9c7cc:0xd9847a}\n// ===== model =====")
rep('t.transparent=!on;t.opacity=on?1:.13;t.depthWrite=on;t.emissive.setHex(sel&&on?EM[k]:0)}','const gh=m.userData.gh||1;t.transparent=!on||gh<1;t.opacity=on?gh:.13;t.depthWrite=on&&gh===1;t.emissive.setHex(sel&&on?EM[k]:0)}')
rep("saraf:['Sistem Saraf (Systema Nervosum)','Cari saraf…']};","saraf:['Sistem Saraf (Systema Nervosum)','Cari saraf…'],organ:['Organ · Sistem Pernapasan (Systema respiratorium)','Cari organ pernapasan…']};")
rep("saraf:'Sistem Saraf'};","saraf:'Sistem Saraf',organ:'Sistem Pernapasan'};")
rep("saraf:'Systema nervosum'};","saraf:'Systema nervosum',organ:'Systema respiratorium'};")
rep("lainnya memakai nama Inggris.'};","lainnya memakai nama Inggris.',organ:'Pilih organ di sidebar. Rangka tampil samar sebagai konteks (tulang rusuk melingkupi paru). Pleura dan mukosa ditampilkan transparan dan hanya bisa dipilih lewat sidebar. Sistem organ lain menyusul.'};")
rep("$('ttl').textContent=NAMES[k][0];","$('ttl').textContent=NAMES[k][0];$('sys').style.display=k==='organ'?'flex':'none';")
rep('MESH[layer].filter(m=>m.visible)','MESH[layer].filter(m=>m.visible&&!m.userData.gh)')
open(P,'w',encoding='utf8').write(h)
print(len(h)/1e6,'MB')
