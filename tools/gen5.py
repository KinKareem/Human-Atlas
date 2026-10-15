import numpy as np,pickle,json,base64,re,collections,cls,detail
K=detail.K
def D(*a): return dict(zip(K,a))
DET={
'testis':D('Gonad pria berpasangan berbentuk oval di dalam skrotum, dibungkus tunika albuginea dan tersusun dari tubulus seminiferus dan sel Leydig.','Spermatogenesis di tubulus seminiferus dan produksi testosteron oleh sel Leydig.','Pleksus testikularis (simpatis T10–T11) dan ramus genital n. genitofemoralis; nyeri alih ke perut bawah.','A. testikularis (cabang aorta abdominal), a. kremaster, a. duktus deferens; v. testikularis (pleksus pampiniformis) bermuara ke v. kava inferior (kanan) dan v. renalis (kiri).','Epididimis, duktus deferens, funikulus spermatikus, skrotum, tunika vaginalis.','Torsio testis (darurat), kanker testis, varikokel (lebih sering sisi kiri), hidrokel, kriptorkismus.'),
'epididymis':D('Struktur melingkar di sisi belakang testis (kaput, korpus, kauda) tempat sperma matang dan disimpan.','Pematangan, penyimpanan, dan pengangkutan sperma menuju duktus deferens.','Pleksus testikularis dan pleksus pelvikus (simpatis); n. ilioinguinalis dan n. genitofemoralis.','A. testikularis dan a. duktus deferens.','Testis, duktus deferens, funikulus spermatikus.','Epididimitis (nyeri skrotum akut), spermatokel, obstruksi pada infertilitas.'),
'deferens':D('Saluran otot tebal sekitar 45 cm dari kauda epididimis, melewati kanalis inguinalis, menyilang ureter, lalu membentuk ampula dan bergabung dengan duktus vesikula seminalis.','Mengangkut sperma ke duktus ejakulatorius saat ejakulasi lewat kontraksi peristaltik.','Simpatis dari pleksus hipogastrik inferior (T10–L2).','A. duktus deferens (cabang a. vesikalis superior).','Funikulus spermatikus, kanalis inguinalis, ureter, kandung kemih, vesikula seminalis.','Vasektomi (pemotongan untuk sterilisasi), kelainan bawaan duktus deferens (pada fibrosis kistik).'),
'ejaculatory':D('Saluran pendek sekitar 2 cm dari penyatuan duktus deferens dan duktus vesikula seminalis, menembus prostat dan bermuara di uretra prostatika.','Menyalurkan sperma dan cairan semen ke uretra saat ejakulasi.','Pleksus hipogastrik inferior (simpatis dan parasimpatis S2–S4).','A. vesikalis inferior dan a. rektalis media.','Prostat, uretra prostatika (kolikulus seminalis), vesikula seminalis, duktus deferens.','Obstruksi duktus ejakulatorius (infertilitas), kista, prostatitis.'),
'seminal':D('Sepasang kelenjar berlekuk di belakang kandung kemih dan di atas prostat.','Menghasilkan sekitar 60–70% cairan semen (fruktosa, prostaglandin, fibrinogen).','Simpatis dari pleksus hipogastrik inferior (L1–L2) untuk emisi.','A. vesikalis inferior dan a. rektalis media.','Kandung kemih, rektum, prostat, ampula duktus deferens.','Vesikulitis, kista, penyebaran kanker prostat ke vesikula seminalis.'),
'prostate':D('Kelenjar fibromuskular seukuran kenari yang mengelilingi uretra proksimal di bawah kandung kemih; zona perifer, transisi, dan sentral.','Menghasilkan cairan prostat (sekitar 20–30% semen) yang mengandung PSA dan membantu motilitas sperma.','Pleksus prostatikus (simpatis T11–L2, parasimpatis S2–S4 lewat n. kavernosus).','A. vesikalis inferior, a. rektalis media, a. pudenda interna; pleksus vena prostatika.','Kandung kemih, uretra, vesikula seminalis, rektum (teraba saat colok dubur), simfisis pubis.','Hiperplasia prostat jinak (zona transisi), karsinoma prostat (zona perifer), prostatitis, pemeriksaan PSA.'),
'corp_cav':D('Dua badan silindris jaringan erektil di sisi punggung penis, dibungkus tunika albuginea.','Terisi darah saat ereksi sehingga penis menjadi kaku.','Parasimpatis (n. kavernosus, S2–S4) merangsang ereksi; n. dorsalis penis (n. pudendus) untuk sensasi.','A. profunda penis dan a. dorsalis penis (cabang a. pudenda interna).','Korpus spongiosum, ramus pubis, otot iskiokavernosus, fasia Buck.','Disfungsi ereksi, penyakit Peyronie, priapismus, fraktur penis.'),
'corp_spong':D('Badan jaringan erektil tunggal di sisi bawah penis yang mengelilingi uretra; ujung depannya membesar menjadi glans.','Menjaga uretra tetap terbuka saat ereksi sehingga ejakulasi dapat lewat.','N. kavernosus (parasimpatis) dan n. dorsalis penis.','A. bulbi penis dan a. uretralis (cabang a. pudenda interna).','Uretra spongiosa, korpus kavernosum, otot bulbospongiosus.','Cedera uretra bulbar (trauma straddle), priapismus, striktur uretra.'),
'glans':D('Ujung penis berbentuk kerucut, perluasan korpus spongiosum, ditutupi preputium; meatus uretra eksternus terbuka di ujungnya.','Daerah paling peka rangsang; saluran keluar urin dan semen.','N. dorsalis penis (cabang n. pudendus, S2–S4).','A. dorsalis penis dan a. bulbi penis.','Korpus spongiosum, preputium, fossa navikularis uretra.','Balanitis, fimosis, parafimosis, hipospadia, karsinoma penis.'),
'urethra':D('Saluran urin dan semen pada pria sekitar 18–20 cm: bagian prostatika, membranosa, dan spongiosa.','Mengalirkan urin dari kandung kemih dan semen saat ejakulasi.','Pleksus prostatikus; n. pudendus (sfingter eksternal volunter).','A. vesikalis inferior, a. rektalis media, a. pudenda interna (a. bulbi penis dan a. uretralis).','Prostat, diafragma urogenital, korpus spongiosum, kandung kemih.','Striktur uretra, uretritis, hipospadia, kerusakan akibat kateterisasi, BPH menekan uretra.')}
NM={'Testis':('Testis','Testis','testis',0,0),'Epididymis':('Epididimis','Epididymis','epididymis',0,0),'Ductus_deferens':('Duktus Deferens','Ductus deferens','deferens',0,0),'Ejaculatory_duct':('Duktus Ejakulatorius','Ductus ejaculatorius','ejaculatory',0,0),'Seminal_gland':('Vesikula Seminalis','Glandula vesiculosa','seminal',0,1),'Prostate':('Prostat','Prostata','prostate',0,1),'Corpus_cavernosum_of_penis':('Korpus Kavernosum Penis','Corpus cavernosum penis','corp_cav',0,2),'Corpus_spongiosum_of_penis':('Korpus Spongiosum Penis','Corpus spongiosum penis','corp_spong',0,2),'Glans_penis':('Glans Penis','Glans penis','glans',0,2),'Urethra':('Uretra Pria','Urethra masculina','urethra',0,2)}
GN=['Testis & Saluran Sperma','Kelenjar Aksesori','Penis & Uretra']
org=pickle.load(open('rep.pkl','rb'))
ms=[]
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
    if side: it['s'].add(side)
sd=lambda s:'kanan & kiri' if s=={'r','l'} else 'kanan' if s=={'r'} else 'kiri' if s=={'l'} else 'garis tengah'
G=[[] for _ in GN]
for b,it in its.items():
    n,l,d,_,g=NM[b]; G[g].append({'id':b,'n':n,'l':l,'e':b.replace('_',' '),'r':GN[g],'s':sd(it['s']),'p':it['p'],'d':d})
groups=[{'g':GN[i],'items':G[i]} for i in range(3)]
print([(g['g'],len(g['items'])) for g in groups],len(meta),sum(m[2] for m in meta),len(blob)/1e6)
json.dump({'g':groups,'DET':DET},open('repro_meta.json','w'),ensure_ascii=False)
open('/mnt/user-data/outputs/data/atlas_repro.json','w').write(json.dumps({'b':base64.b64encode(blob).decode(),'m':M},separators=(',',':')))
