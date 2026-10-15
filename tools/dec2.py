import numpy as np, pickle, json, base64, cls
out=pickle.load(open('ms.pkl','rb'))
def dec(V,F,target):
    if len(F)<=target: return V,F
    mn,mx=V.min(0),V.max(0); ext=(mx-mn).max()
    minf=min(len(F),60)
    lo,hi=ext/3000,ext/1.5; best=None; fall=None
    for _ in range(12):
        h=(lo*hi)**.5
        q=np.floor((V-mn)/h).astype(np.int64)
        u,inv=np.unique(q[:,0]*4194304+q[:,1]*2048+q[:,2],return_inverse=True)
        nf=inv[F]; ok=(nf[:,0]!=nf[:,1])&(nf[:,1]!=nf[:,2])&(nf[:,0]!=nf[:,2]); nf=nf[ok]
        if len(nf):
            s=np.sort(nf,1).astype(np.int64);N=len(u)
            nf=nf[np.unique(s[:,0]*N*N+s[:,1]*N+s[:,2],return_index=True)[1]]
        if len(nf)>target: lo=h
        elif len(nf)<minf: hi=h; fall=fall or (inv,nf,len(u))
        else: hi=h; best=(inv,nf,len(u))
    r=best or fall
    if r is None or len(r[1])==0: return V,F
    inv,nf,nu=r
    cnt=np.bincount(inv,minlength=nu)
    nv=np.stack([np.bincount(inv,weights=V[:,k],minlength=nu) for k in range(3)],1)/cnt[:,None]
    used=np.unique(nf); rm=-np.ones(nu,int); rm[used]=np.arange(len(used))
    return nv[used],rm[nf]
T={'otot':260000,'saraf':150000}
for layer,items in out.items():
    raw=sum(len(a[2]) for a in items); ms=[]
    for x,V,F in items:
        used=np.unique(F); r=-np.ones(len(V),int); r[used]=np.arange(len(used)); V=V[used].astype(np.float64); F=r[F]
        t=max(100,int(len(F)/raw*T[layer])); V2,F2=dec(V,F,t)
        if len(V2)>65000: V2,F2=dec(V2,F2,len(F2)//3)
        ms.append((x,V2,F2))
    A=np.vstack([m[1] for m in ms]); mn=A.min(0); sc=float((A.max(0)-mn).max())
    vb=bytearray(); fb=bytearray(); meta=[]; X=[]
    for x,V,F in ms:
        q=np.round((V-mn)/sc*65535).astype(np.uint16)
        meta.append([cls.names[x[0]],len(V),len(F),len(vb)//2,len(fb)//2]); X.append(x); vb+=q.tobytes(); fb+=F.astype(np.uint16).tobytes()
    nv=len(vb)//2
    for m in meta: m[4]+=nv
    blob=bytes(vb)+bytes(fb)
    print(layer,len(ms),'tris',sum(m[2] for m in meta),'MB',len(blob)/1e6,flush=True)
    json.dump({'mn':mn.tolist(),'sc':sc,'meta':meta},open(f'meta_{layer}.json','w'))
    open(f'blob_{layer}.b64','w').write(base64.b64encode(blob).decode())
print('done')
