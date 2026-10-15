import numpy as np,pickle,json,base64,collections,cls,detail
K=detail.K
def D(*a): return dict(zip(K,a))
DET={
'kidney':D('Sepasang organ berbentuk kacang di ruang retroperitoneal setinggi T12–L3 (ginjal kanan sedikit lebih rendah); terdiri dari korteks, medula (piramid), kaliks, dan hilus; sekitar satu juta nefron per ginjal.','Menyaring darah dan membentuk urin, mengatur cairan, elektrolit, dan tekanan darah (renin), memproduksi eritropoietin, mengaktifkan vitamin D.','Pleksus renalis (simpatis T10–L1); nyeri ginjal dirasakan di pinggang dan menjalar ke selangkangan.','A. renalis (cabang aorta abdominal, sekitar 20% curah jantung), a. segmentalis dan interlobaris; v. renalis ke v. kava inferior.','Kelenjar suprarenal (atas), hati (kanan), limpa (kiri), kolon, pankreas, otot psoas dan kuadratus lumborum, rusuk 11–12.','Batu ginjal, pielonefritis, gagal ginjal akut dan kronis, karsinoma sel ginjal, penyakit ginjal polikistik, hidronefrosis.'),
'renal_pelvis':D('Rongga berbentuk corong di hilus ginjal tempat bertemunya kaliks mayor dan minor, menyambung ke ureter.','Menampung urin dari kaliks dan menyalurkannya ke ureter.','Pleksus renalis (simpatis dan serabut sensorik T10–L1).','A. renalis (cabang pelvis) dan a. ureterika.','Kaliks renalis, sinus renalis, pembuluh ginjal, ureter (sambungan ureteropelvik).','Hidronefrosis, batu di sambungan ureteropelvik (kolik ginjal), pielitis.'),
'ureter':D('Tabung otot sekitar 25 cm dari pelvis renalis ke kandung kemih; retroperitoneal, menyilang pembuluh iliaka dan di bawah a. uterina atau duktus deferens.','Menyalurkan urin ke kandung kemih dengan gerak peristaltik.','Pleksus renalis, ureterikus, dan hipogastrik (simpatis T10–L2, parasimpatis S2–S4); nyeri kolik menjalar ke pinggang dan selangkangan.','A. renalis, a. gonadalis, cabang aorta, a. iliaka komunis, a. vesikalis inferior.','M. psoas, pembuluh iliaka dan gonadal, kandung kemih (muara ureter), duktus deferens pada pria.','Batu ureter pada tiga penyempitan (ureteropelvik, tepi pelvis, ureterovesikal), cedera ureter saat operasi pelvis, refluks vesikoureter.'),
'bladder':D('Kantung otot (detrusor) di belakang simfisis pubis dengan apeks, korpus, fundus, dan leher; trigonum vesika di dasarnya.','Menampung urin (sekitar 400–600 mL) dan mengosongkannya saat berkemih.','Parasimpatis S2–S4 (kontraksi detrusor), simpatis T10–L2 (relaksasi detrusor, penutupan leher), n. pudendus (sfingter eksternal volunter).','A. vesikalis superior dan inferior (cabang a. iliaka interna); v. vesikalis ke v. iliaka interna.','Simfisis pubis, prostat (pria) atau vagina dan uterus (wanita), rektum, ureter, uretra.','Infeksi saluran kemih (sistitis), karsinoma kandung kemih, batu kandung kemih, retensi urin, kandung kemih neurogenik.')}
NM={'Kidney':('Ginjal','Ren','kidney',0),'Renal_pelvis':('Pelvis Renalis','Pelvis renalis','renal_pelvis',0),'Ureter':('Ureter','Ureter','ureter',1),'Urinary_bladder':('Kandung Kemih','Vesica urinaria','bladder',1),'Urethra':('Uretra Pria','Urethra masculina','urethra',1)}
GN=['Ginjal','Saluran Kemih']
org=pickle.load(open('uri.pkl','rb')); seen=set(); ms=[]
for i,V,F in org:
    k=(V.shape,round(float(V.sum()),3))
    if k in seen: continue
    seen.add(k); used=np.unique(F); r=-np.ones(len(V),int); r[used]=np.arange(len(used)); ms.append((cls.names[i],V[used].astype(np.float64),r[F]))
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
    n,l,d,g=NM[b]; G[g].append({'id':b,'n':n,'l':l,'e':b.replace('_',' '),'r':GN[g],'s':sd(it['s']),'p':it['p'],'d':d})
groups=[{'g':GN[i],'items':G[i]} for i in range(2)]
print([(g['g'],len(g['items'])) for g in groups],len(meta),sum(m[2] for m in meta),len(blob)/1e6)
json.dump({'g':groups,'DET':DET},open('urin_meta.json','w'),ensure_ascii=False)
open('/mnt/user-data/outputs/data/atlas_urin.json','w').write(json.dumps({'b':base64.b64encode(blob).decode(),'m':M},separators=(',',':')))
