import numpy as np,pickle,json,base64,collections,re,cls
info=pickle.load(open('vs_info.pkl','rb'))
isv=lambda b:bool(re.search(r'vein|vena|sinus|venous|plexus',b,re.I))
LAY={'vsKa':'Kepala & Leher (Arteri)','vsKv':'Kepala & Leher (Vena)','vsTo':'Toraks','vsAb':'Abdomen & Pelvis','vsLe':'Lengan & Tangan','vsTu':'Tungkai & Kaki'}
RK={'Kepala & Leher':None,'Toraks':'vsTo','Abdomen & Pelvis':'vsAb','Lengan & Tangan':'vsLe','Tungkai & Kaki':'vsTu'}
L={k:[] for k in LAY}
def split(V,F):
    if len(V)<65000: return [(V,F)]
    cs=100000
    while True:
        out=[]
        for s in range(0,len(F),cs):
            f=F[s:s+cs]; u=np.unique(f); r=-np.ones(len(V),int); r[u]=np.arange(len(u)); out.append((V[u],r[f]))
        if max(len(o[0]) for o in out)<65000: return out
        cs//=2
for i,reg,nv,nf in info:
    z=np.load(f'vs/{i}.npz'); V=z['V'].astype(np.float64); F=z['F'].astype(np.int64)
    used=np.unique(F); r=-np.ones(len(V),int); r[used]=np.arange(len(used)); V=V[used]; F=r[F]
    b=cls.split(cls.names[i])[0]
    k=('vsKv' if isv(b) else 'vsKa') if reg=='Kepala & Leher' else RK[reg]
    for v,f in split(V,F): L[k].append((cls.names[i],v,f))
GEN={'artery_gen':dict(zip(['desc','fn','nerve','blood','rel','clin'],['Arteri membawa darah dari jantung ke jaringan; dindingnya terdiri dari tunika intima, media (otot polos dan elastin), dan adventisia. Rincian untuk pembuluh ini belum ditulis satu per satu.','Menyalurkan darah beroksigen (kecuali a. pulmonalis) dengan tekanan tinggi ke organ dan jaringan yang dilayaninya.','Serabut simpatis vasomotor di tunika adventisia mengatur diameter pembuluh; baroreseptor pada arteri besar tertentu.','Vasa vasorum (pembuluh kecil) memberi nutrisi pada dinding arteri besar.','Biasanya berjalan bersama vena dan saraf dalam berkas neurovaskular; letak tepatnya bergantung pada nama pembuluh.','Aterosklerosis, aneurisma, emboli, trombosis, diseksi, dan cedera trauma; gejala bergantung pada daerah yang dipasok.'])),
'vein_gen':dict(zip(['desc','fn','nerve','blood','rel','clin'],['Vena membawa darah kembali ke jantung; dindingnya lebih tipis dengan katup di banyak vena ekstremitas, dan sinus dura tidak berotot. Rincian untuk pembuluh ini belum ditulis satu per satu.','Mengalirkan darah kembali ke jantung dengan tekanan rendah (kecuali v. pulmonalis); berfungsi pula sebagai reservoir darah.','Serabut simpatis vasomotor mengatur venokonstriksi; vena dalam mengikuti persarafan struktur di dekatnya.','Vasa vasorum pada vena besar.','Vena dalam biasanya menyertai arteri; vena superfisial berjalan di jaringan bawah kulit.','Trombosis vena dalam, varises, tromboflebitis, insufisiensi vena, trombosis sinus (pada sinus dura).']))}
dj=lambda x:json.dumps(x,ensure_ascii=False,separators=(',',':'))
groups={};tot={}
for k,ms in L.items():
    A=np.vstack([m[1] for m in ms]); mn=A.min(0); sc=float((A.max(0)-mn).max())
    vb=bytearray(); fb=bytearray(); meta=[]
    for n,V,F in ms:
        q=np.round((V-mn)/sc*65535).astype(np.uint16); meta.append([n,len(V),len(F),len(vb)//2,len(fb)//2]); vb+=q.tobytes(); fb+=F.astype(np.uint16).tobytes()
    nv=len(vb)//2
    for m in meta: m[4]+=nv
    blob=bytes(vb)+bytes(fb)
    s=dj({'b':base64.b64encode(blob).decode(),'m':{'mn':mn.tolist(),'sc':sc,'meta':meta}})
    open(f'/mnt/user-data/outputs/data/atlas_{k}.json','w').write(s)
    its=collections.OrderedDict()
    for i,m in enumerate(meta):
        b,sfx,side,t=cls.split(m[0]); it=its.setdefault(b,{'p':[],'s':set()}); it['p'].append(i)
        if side: it['s'].add(side)
    sd=lambda s:'kanan & kiri' if s=={'r','l'} else 'kanan' if s=={'r'} else 'kiri' if s=={'l'} else 'garis tengah'
    items=sorted([{'id':b,'n':b.replace('_',' ').strip('()'),'l':'','e':b.replace('_',' '),'r':LAY[k],'s':sd(it['s']),'p':it['p'],'d':'vein_gen' if isv(b) else 'artery_gen','g':1} for b,it in its.items()],key=lambda o:o['n'].lower())
    gs=[];cur=[]
    for o in items:
        cur.append(o)
        if len(cur)>=22: gs.append(cur);cur=[]
    if cur: gs.append(cur)
    groups[k]=[{'g':'%s – %s'%(g[0]['n'][:1].upper(),g[-1]['n'][:1].upper()) if g[0]['n'][:1].upper()!=g[-1]['n'][:1].upper() else g[0]['n'][:1].upper(),'items':g} for g in gs]
    tot[k]=(len(ms),len(items),len(s)/1e6,sum(m[2] for m in meta))
print(tot)
json.dump({'g':groups,'DET':GEN,'LAY':LAY},open('vs_meta.json','w'),ensure_ascii=False)
