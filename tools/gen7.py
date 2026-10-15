import numpy as np,pickle,json,base64,collections,cls,detail
K=detail.K
def D(*a): return dict(zip(K,a))
DET={
'hypothalamus':D('Bagian diensefalon di bawah talamus yang membentuk dasar dan dinding ventral ventrikel ketiga; terhubung ke hipofisis lewat infundibulum.','Pusat integrasi saraf dan endokrin: mengatur suhu, lapar, haus, tidur, emosi, dan hormon hipofisis (releasing hormone, ADH, oksitosin).','Hubungan dengan sistem limbik, batang otak, dan sistem saraf otonom; traktus hipotalamohipofisial ke neurohipofisis.','Lingkaran Willis (a. komunikans posterior dan anterior, a. serebri posterior); sistem portal hipotalamo-hipofisial.','Kiasma optikum, hipofisis, talamus, ventrikel ketiga, korpus mamilare.','Diabetes insipidus sentral, gangguan termoregulasi, hipopituitarisme, tumor (kraniofaringioma, glioma).'),
'adenohyp':D('Lobus anterior hipofisis (sekitar 75%), berasal dari kantung Rathke; terdiri dari pars distalis, tuberalis, dan intermedia di sela tursika.','Mensekresi GH, ACTH, TSH, FSH, LH, prolaktin, dan MSH di bawah kendali hormon hipotalamus.','Diatur hormon hipotalamus lewat sistem portal, bukan oleh serabut saraf langsung.','A. hipofisial superior (cabang a. karotis interna) melalui sistem portal hipotalamo-hipofisial.','Neurohipofisis, kiasma optikum (di atas), sinus sfenoid (di bawah), sinus kavernosus, hipotalamus.','Adenoma hipofisis (prolaktinoma tersering), akromegali, penyakit Cushing, hipopituitarisme, hemianopsia bitemporal.'),
'neurohyp':D('Lobus posterior hipofisis, perpanjangan saraf dari hipotalamus (pars nervosa dan infundibulum).','Menyimpan dan melepas ADH (vasopresin) dan oksitosin yang dibuat di hipotalamus.','Akson nukleus supraoptik dan paraventrikular hipotalamus (traktus hipotalamohipofisial).','A. hipofisial inferior (cabang a. karotis interna).','Adenohipofisis, hipotalamus, tangkai hipofisis, sela tursika.','Diabetes insipidus (kurang ADH), SIADH, sindrom Sheehan.'),
'pineal':D('Kelenjar kecil berbentuk kerucut di garis tengah, di belakang ventrikel ketiga dekat talamus; sering mengalami kalsifikasi seiring usia.','Menghasilkan melatonin yang mengatur ritme sirkadian dan tidur-bangun.','Simpatis dari ganglion servikal superior; terhubung ke retina lewat nukleus suprakiasmatik.','A. koroidalis posterior medial (cabang a. serebri posterior).','Talamus, kolikulus superior, ventrikel ketiga, komisura habenula dan posterior.','Tumor pineal (pinealoma, germinoma), sindrom Parinaud, gangguan tidur, kalsifikasi pineal (penanda garis tengah radiologi).'),
'thyroid':D('Kelenjar berbentuk kupu-kupu di leher depan di bawah laring dengan dua lobus yang dihubungkan isthmus di depan cincin trakea 2–4.','Memproduksi tiroksin (T4) dan triiodotironin (T3) untuk metabolisme, serta kalsitonin yang menurunkan kalsium.','Simpatis dari ganglion servikal; n. laringeus rekuren dan superior berjalan di dekatnya.','A. tiroidea superior (a. karotis eksterna) dan inferior (trunkus tirokervikalis), kadang a. tiroidea ima.','Trakea, laring, kelenjar paratiroid (di belakang), n. laringeus rekuren, a. karotis komunis.','Hipertiroidisme (Graves), hipotiroidisme (Hashimoto), goiter, nodul dan kanker tiroid, cedera n. laringeus rekuren saat tiroidektomi.'),
'parathyroid':D('Empat kelenjar kecil sebesar butir beras di permukaan belakang kelenjar tiroid (dua superior dan dua inferior).','Mensekresi hormon paratiroid (PTH) yang menaikkan kadar kalsium darah lewat tulang, ginjal, dan usus.','Simpatis dari ganglion servikal; fungsi diatur umpan balik kalsium, bukan oleh saraf.','A. tiroidea inferior (terutama) dan a. tiroidea superior.','Permukaan belakang lobus tiroid, n. laringeus rekuren, esofagus, trakea.','Hiperparatiroidisme (adenoma, batu ginjal, osteoporosis), hipoparatiroidisme (hipokalsemia pasca tiroidektomi), tetani.'),
'adrenal':D('Sepasang kelenjar segitiga di atas kutub atas ginjal, terdiri dari korteks (zona glomerulosa, fasikulata, retikularis) dan medula.','Korteks: kortisol, aldosteron, androgen; medula: epinefrin dan norepinefrin (respons stres).','Medula dipersarafi langsung oleh serabut simpatis preganglionik (n. splanknikus, T10–L1).','A. suprarenal superior, media, inferior (dari a. frenika inferior, aorta, a. renalis); v. suprarenalis ke v. kava inferior (kanan) atau v. renalis kiri.','Kutub atas ginjal, diafragma, hati dan v. kava inferior (kanan), pankreas dan limpa (kiri).','Sindrom Cushing, penyakit Addison, hiperaldosteronisme (sindrom Conn), feokromositoma, insufisiensi adrenal.'),
'thymus':D('Organ limfoid bilobus di mediastinum anterior atas, di belakang sternum; besar pada anak lalu mengecil dan digantikan lemak setelah pubertas.','Tempat pematangan sel T dan sumber hormon timosin.','N. vagus, trunkus simpatikus, dan cabang kecil n. frenikus.','A. torakika interna (cabang timus), a. tiroidea inferior; v. timika ke v. brakiosefalika kiri.','Sternum, perikardium dan arkus aorta, v. brakiosefalika kiri, trakea.','Timoma (terkait miastenia gravis), sindrom DiGeorge (aplasia timus), hipoplasia timus pada imunodefisiensi.')}
NM={'Hypothalamus':('Hipotalamus','Hypothalamus','hypothalamus',0,0),'Adenohypophysis':('Hipofisis Anterior (Adenohipofisis)','Adenohypophysis','adenohyp',0,0),'Neurohypophysis':('Hipofisis Posterior (Neurohipofisis)','Neurohypophysis','neurohyp',0,0),'Pineal_gland':('Kelenjar Pineal','Glandula pinealis','pineal',0,0),'Thyroid_gland':('Kelenjar Tiroid','Glandula thyroidea','thyroid',0,1),'Superior_parathyroid_gland':('Kelenjar Paratiroid Superior','Glandula parathyroidea superior','parathyroid',1,1),'Inferior_parathyroid_gland':('Kelenjar Paratiroid Inferior','Glandula parathyroidea inferior','parathyroid',1,1),'Suprarenal_gland':('Kelenjar Suprarenal (Adrenal)','Glandula suprarenalis','adrenal',0,3),'Left_lobe_of_thymus':('Timus (Lobus Kiri)','Lobus sinister thymi','thymus',1,2),'Right_lobe_of_thymus':('Timus (Lobus Kanan)','Lobus dexter thymi','thymus',1,2)}
GN=['Otak & Kelenjar Hipofisis','Leher','Toraks','Abdomen']
org=pickle.load(open('end.pkl','rb')); ms=[]
for i,V,F in org:
    used=np.unique(F); r=-np.ones(len(V),int); r[used]=np.arange(len(used)); ms.append((cls.names[i],V[used].astype(np.float64),r[F]))
A=np.vstack([m[1] for m in ms]); mn=A.min(0); sc=float((A.max(0)-mn).max())
vb=bytearray(); fb=bytearray(); meta=[]
for n,V,F in ms:
    q=np.round((V-mn)/sc*65535).astype(np.uint16); meta.append([n,len(V),len(F),len(vb)//2,len(fb)//2]); vb+=q.tobytes(); fb+=F.astype(np.uint16).tobytes()
nv=len(vb)//2
for m in meta: m[4]+=nv
blob=bytes(vb)+bytes(fb); M={'mn':mn.tolist(),'sc':sc,'meta':meta}
its=collections.OrderedDict()
for i,m in enumerate(meta):
    b,s,side,t=cls.split(m[0]); it=its.setdefault(b,{'p':[],'s':set()}); it['p'].append(i)
    sd=side or ('r' if b.startswith('Right') else 'l' if b.startswith('Left') else '')
    if sd: it['s'].add(sd)
sdf=lambda s:'kanan & kiri' if s=={'r','l'} else 'kanan' if s=={'r'} else 'kiri' if s=={'l'} else 'garis tengah'
G=[[] for _ in GN]
for b,it in its.items():
    n,l,d,gen,g=NM[b]; o={'id':b,'n':n,'l':l,'e':b.replace('_',' '),'r':GN[g],'s':sdf(it['s']),'p':it['p'],'d':d}
    if gen: o['g']=1
    G[g].append(o)
groups=[{'g':GN[i],'items':G[i]} for i in range(4)]
print([(g['g'],len(g['items'])) for g in groups],len(meta),sum(m[2] for m in meta),len(blob)/1e6)
json.dump({'g':groups,'DET':DET},open('endo_meta.json','w'),ensure_ascii=False)
open('/mnt/user-data/outputs/data/atlas_endo.json','w').write(json.dumps({'b':base64.b64encode(blob).decode(),'m':M},separators=(',',':')))
