import json,re,collections,cls,detail
from bones import info as binfo, R as BR
def sidestr(s): return 'kanan & kiri' if s=={'r','l'} else 'kanan' if s=={'r'} else 'kiri' if s=={'l'} else 'garis tengah'
def pack(layer):
    M=json.load(open(f'meta_{layer}.json')); return M
def items_by_base(meta):
    d=collections.OrderedDict()
    for i,m in enumerate(meta):
        b,s,side,t=cls.split(m[0]); it=d.setdefault(b,{'p':[],'s':set()}); it['p'].append(i)
        if side: it['s'].add(side)
    return d
# ---- rangka (struktur sama seperti sebelumnya)
Mr=json.load(open('meta.json')); rb=collections.OrderedDict()
for idx,m in enumerate(Mr['meta']):
    n=m[0]; b=re.sub(r'\.(r|l)$','',n); s=n[len(b)+1:] if n!=b else ''
    it=rb.setdefault(b,{'p':[],'s':set()}); it['p'].append(idx)
    if s: it['s'].add(s)
G=[[] for _ in BR]
for b,it in rb.items():
    i,l,rg,key,d0=binfo(b); d=detail.dkey(b) or d0
    o={'id':b,'n':i,'l':l,'e':b.replace('_',' '),'r':BR[rg],'s':sidestr(it['s']),'p':it['p']}
    if d: o['d']=d
    if d in detail.GEN: o['g']=1
    G[rg].append((key,o))
GR=[{'g':BR[k],'items':[o for _,o in sorted(G[k],key=lambda x:x[0])]} for k in range(len(BR))]
# ---- otot
MUS={'biceps_brachii':('Otot Bisep Brakii','Musculus biceps brachii'),'triceps_brachii':('Otot Trisep Brakii','Musculus triceps brachii'),'deltoid':('Otot Deltoid','Musculus deltoideus'),'pectoralis_major':('Otot Pektoralis Mayor','Musculus pectoralis major'),'pectoralis_minor':('Otot Pektoralis Minor','Musculus pectoralis minor'),'trapezius':('Otot Trapezius','Musculus trapezius'),'latissimus_dorsi':('Otot Latissimus Dorsi','Musculus latissimus dorsi'),'rectus_abdominis':('Otot Rektus Abdominis','Musculus rectus abdominis'),'external_abdominal_oblique':('Otot Oblik Eksternus Abdomen','Musculus obliquus externus abdominis'),'internal_abdominal_oblique':('Otot Oblik Internus Abdomen','Musculus obliquus internus abdominis'),'transversus_abdominis':('Otot Transversus Abdominis','Musculus transversus abdominis'),'diaphragm':('Diafragma','Diaphragma'),'sternocleidomastoid':('Otot Sternokleidomastoid','Musculus sternocleidomastoideus'),'masseter':('Otot Masseter','Musculus masseter'),'temporalis':('Otot Temporalis','Musculus temporalis'),'gluteus_maximus':('Otot Gluteus Maksimus','Musculus gluteus maximus'),'gluteus_medius':('Otot Gluteus Medius','Musculus gluteus medius'),'gluteus_minimus':('Otot Gluteus Minimus','Musculus gluteus minimus'),'rectus_femoris':('Otot Rektus Femoris','Musculus rectus femoris'),'vastus_lateralis':('Otot Vastus Lateralis','Musculus vastus lateralis'),'vastus_medialis':('Otot Vastus Medialis','Musculus vastus medialis'),'vastus_intermedius':('Otot Vastus Intermedius','Musculus vastus intermedius'),'sartorius':('Otot Sartorius','Musculus sartorius'),'biceps_femoris':('Otot Bisep Femoris','Musculus biceps femoris'),'semitendinosus':('Otot Semitendinosus','Musculus semitendinosus'),'semimembranosus':('Otot Semimembranosus','Musculus semimembranosus'),'soleus':('Otot Soleus','Musculus soleus'),'tibialis_anterior':('Otot Tibialis Anterior','Musculus tibialis anterior'),'gracilis':('Otot Gracilis','Musculus gracilis'),'psoas_major':('Otot Psoas Mayor','Musculus psoas major'),'iliacus':('Otot Iliakus','Musculus iliacus'),'serratus_anterior':('Otot Serratus Anterior','Musculus serratus anterior'),'brachioradialis':('Otot Brakioradialis','Musculus brachioradialis'),'brachialis':('Otot Brakialis','Musculus brachialis'),'orbicularis_oculi':('Otot Orbikularis Okuli','Musculus orbicularis oculi'),'levator_scapulae':('Otot Levator Skapula','Musculus levator scapulae'),'supraspinatus':('Otot Supraspinatus','Musculus supraspinatus'),'infraspinatus':('Otot Infraspinatus','Musculus infraspinatus'),'subscapularis':('Otot Subskapularis','Musculus subscapularis'),'teres_major':('Otot Teres Mayor','Musculus teres major'),'teres_minor':('Otot Teres Minor','Musculus teres minor'),'platysma':('Otot Platisma','Platysma'),'erector_spinae':('Otot Erector Spinae','Musculus erector spinae')}
MR=['Kepala & Leher','Toraks & Punggung','Abdomen & Pelvis','Lengan & Tangan','Tungkai & Kaki','Lainnya']
MRX=[('foot',4,r'of_foot|hallucis|plantar|plantaris|tibialis|fibularis|peroneus|gastrocnemius|soleus|popliteus|digitorum_longus|digitorum_brevis'),
('hand',3,r'pollicis|carpi|indicis|brachii|brachial|deltoid|supraspinatus|infraspinatus|teres|subscapularis|coracobrachialis|anconeus|pronator|supinator|palmaris|lumbrical|thenar|opponens|of_hand|digitorum|digiti_minimi|interossei'),
('head',0,r'splenius|capitis|colli|scalen|sternocleido|platysma|hyoid|digastric|stylo|genio|masseter|temporalis|pterygoid|bucinator|buccinator|zygomatic|orbicularis|frontalis|occipitalis|auricular|nasalis|procerus|corrugator|depressor|levator_(anguli|labii|palpebrae|nasolabialis)|risorius|mentalis|constrictor|pharyng|laryn|crico|arytenoid|stapedius|tympani|veli|palat|lingu|glossus|(lateral|medial|superior|inferior)_rectus|(superior|inferior)_oblique|tarsus|nasi'),
('trunk',1,r'pectoralis|serratus|intercostal|diaphragm|trapezius|latissimus|rhomboid|levator_scapulae|erector|spinalis|longissimus|iliocostalis|multifidus|semispinalis|rotatores|subcostal|transversus_thoracis|interspinales|intertransvers|levatores|thoracis'),
('abd',2,r'abdomin|oblique|quadratus_lumborum|psoas|iliacus|levator_ani|coccygeus|sphincter|perine|bulbospongiosus|ischiocavernosus|cremaster|pubo|obturator_internus|piriformis|anal'),
('leg',4,r'gluteus|femoris|vastus|sartorius|gracilis|adductor|gemell|tensor_fasciae|semitendinosus|semimembranosus|obturator_externus|pectineus|quadratus_femoris')]
def mreg(l):
    for _,r,p in MRX:
        if re.search(p,l): return r
    return 5
def norm(b): return b.lower().replace('_muscle','')
def cleaned(b): return b.replace('_',' ')
def build_mus():
    meta=json.load(open('meta_otot.json'))['meta']; its=items_by_base(meta); g=[[] for _ in MR]
    for b,it in its.items():
        k=norm(b); n,l=MUS.get(k,(cleaned(b),'')); rg=mreg(k)
        d=None;gen=0
        if k=='biceps_brachii': d='biceps'
        elif 'biceps_brachii' in k: d='biceps';gen=1
        elif 'deltoid' in k: d='deltoid';gen=1
        elif re.search(r'rectus_femoris|vastus',k): d='quadriceps';gen=1
        o={'id':b,'n':n,'l':l,'e':cleaned(b),'r':MR[rg],'s':sidestr(it['s']),'p':it['p']}
        if d: o['d']=d
        if gen: o['g']=1
        g[rg].append(o)
    return [{'g':MR[i],'items':sorted(g[i],key=lambda o:o['n'])} for i in range(len(MR))]
# ---- saraf
NER={'median_nerve':('Saraf Median','Nervus medianus'),'ulnar_nerve':('Saraf Ulnaris','Nervus ulnaris'),'radial_nerve':('Saraf Radialis','Nervus radialis'),'musculocutaneous_nerve':('Saraf Muskulokutaneus','Nervus musculocutaneus'),'axillary_nerve':('Saraf Aksilaris','Nervus axillaris'),'sciatic_nerve':('Saraf Iskiadikus','Nervus ischiadicus'),'femoral_nerve':('Saraf Femoralis','Nervus femoralis'),'tibial_nerve':('Saraf Tibialis','Nervus tibialis'),'common_fibular_nerve':('Saraf Peroneus Komunis','Nervus fibularis communis'),'obturator_nerve':('Saraf Obturatorius','Nervus obturatorius'),'phrenic_nerve':('Saraf Frenikus','Nervus phrenicus'),'vagus_nerve_(x)':('Saraf Vagus (X)','Nervus vagus'),'facial_nerve_(vii)':('Saraf Fasialis (VII)','Nervus facialis'),'trigeminal_nerve_(v)':('Saraf Trigeminus (V)','Nervus trigeminus'),'optic_nerve_(ii)':('Saraf Optikus (II)','Nervus opticus'),'oculomotor_nerve_(iii)':('Saraf Okulomotorius (III)','Nervus oculomotorius'),'trochlear_nerve_(iv)':('Saraf Troklearis (IV)','Nervus trochlearis'),'abducens_nerve_(vi)':('Saraf Abdusens (VI)','Nervus abducens'),'vestibulocochlear_nerve_(viii)':('Saraf Vestibulokoklearis (VIII)','Nervus vestibulocochlearis'),'glossopharyngeal_nerve_(ix)':('Saraf Glosofaringeus (IX)','Nervus glossopharyngeus'),'accessory_nerve_(xi)':('Saraf Aksesorius (XI)','Nervus accessorius'),'hypoglossal_nerve_(xii)':('Saraf Hipoglosus (XII)','Nervus hypoglossus'),'olfactory_nerve_(i)':('Saraf Olfaktorius (I)','Nervus olfactorius'),'spinal_cord':('Medula Spinalis','Medulla spinalis'),'intercostal_nerves':('Saraf Interkostalis','Nervi intercostales'),'brachial_plexus':('Pleksus Brakialis','Plexus brachialis'),'lumbar_plexus':('Pleksus Lumbalis','Plexus lumbalis'),'sacral_plexus':('Pleksus Sakralis','Plexus sacralis')}
NR=['Saraf Kranial & Kepala-Leher','Medula Spinalis & Pleksus','Lengan & Tangan','Toraks & Abdomen','Pelvis & Tungkai','Lainnya']
NRX=[(2,r'brachial|median|ulnar|radial|musculocutaneous|axillary|subscapular|thoracodorsal|long_thoracic|suprascapular|pectoral|antebrachial|palmar|dorsal_scapular|digital_.*hand'),
(0,r'\((i|ii|iii|iv|v|vi|vii|viii|ix|x|xi|xii)\)|optic|oculomotor|trochlear|trigeminal|abducens|facial|vestibulocochlear|glossopharyngeal|vagus|accessory|hypoglossal|olfactory|ophthalmic|maxillary|mandibular|lingual|auriculotemporal|mental|infraorbital|supraorbital|frontal|lacrimal|nasociliary|buccal|alveolar|palatine|zygomatic|chorda|cervical|occipital|supraclavicular|auricular|laryngeal|pharyngeal|cranial'),
(3,r'intercostal|subcostal|phrenic|splanchnic|iliohypogastric|ilioinguinal|genitofemoral|thoracic|cardiac|pulmonary|celiac|mesenteric|hypogastric|lumbar'),
(4,r'sciatic|tibial|fibular|peroneal|femoral|obturator|sural|saphenous|plantar|gluteal|pudendal|sacral|pelvic|crural|calcaneal|perineal|coccygeal|genicular|foot|thigh|leg'),
(1,r'spinal|cauda|conus|root|ganglion|plexus|trunk|ramus|rami|sympathetic')]
def nreg(l):
    for r,p in NRX:
        if re.search(p,l): return r
    return 5
def build_ner():
    meta=json.load(open('meta_saraf.json'))['meta']; its=items_by_base(meta); g=[[] for _ in NR]
    for b,it in its.items():
        k=b.lower(); n,l=NER.get(k,(cleaned(b),'')); rg=nreg(k); d=None
        if k=='median_nerve': d='median'
        elif k=='sciatic_nerve': d='ischiadicus'
        elif k=='spinal_cord': d='medulla'
        o={'id':b,'n':n,'l':l,'e':cleaned(b),'r':NR[rg],'s':sidestr(it['s']),'p':it['p']}
        if d: o['d']=d
        g[rg].append(o)
    return [{'g':NR[i],'items':sorted(g[i],key=lambda o:o['n'])} for i in range(len(NR))]
GO=build_mus(); GN=build_ner()
print('otot',[(x['g'],len(x['items'])) for x in GO]); print('saraf',[(x['g'],len(x['items'])) for x in GN])
DET=json.load(open('old_det.json'))
for k,v in detail.R.items(): DET[k]=dict(zip(detail.K,v))
for k in ['cranium','vertebra','kosta','sternum']: pass
BLd={}
for name,meta_f,blob_f,g in [('rangka','meta.json','blob.b64',GR),('otot','meta_otot.json','blob_otot.b64',GO),('saraf','meta_saraf.json','blob_saraf.b64',GN)]:
    BLd[name]=(open(blob_f).read(),json.load(open(meta_f)),g)
parts=['<script>const BL={']
parts.append(','.join('%s:{b:"%s",m:%s,g:%s}'%(k,b,json.dumps(m,separators=(',',':')),json.dumps(g,ensure_ascii=False,separators=(',',':'))) for k,(b,m,g) in BLd.items()))
parts.append('};const DET=%s;</script>'%json.dumps(DET,ensure_ascii=False,separators=(',',':')))
html=open('tpl.html',encoding='utf8').read().replace('%%DATA%%',''.join(parts))
open('/mnt/user-data/outputs/anatomi-rangka.html','w',encoding='utf8').write(html)
print(len(html)/1e6,'MB')
miss=[x['id'] for g in GR for x in g['items'] if 'd' not in x]; print('rangka tanpa detail',len(miss))
