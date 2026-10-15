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
