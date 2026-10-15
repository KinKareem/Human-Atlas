import numpy as np, pickle, json, base64
objs=pickle.load(open('bones.pkl','rb'))
def dec(V,F,target):
    if len(F)<=target: return V,F
    mn,mx=V.min(0),V.max(0); ext=(mx-mn).max()
    lo,hi=ext/2000,ext/2
    best=None
    for _ in range(14):
        h=(lo*hi)**.5
        q=np.floor((V-mn)/h).astype(np.int64)
        key=q[:,0]*4000000+q[:,1]*2000+q[:,2]
        u,inv=np.unique(key,return_inverse=True)
        nf=inv[F]
        ok=(nf[:,0]!=nf[:,1])&(nf[:,1]!=nf[:,2])&(nf[:,0]!=nf[:,2])
        nf=nf[ok]
        s=np.sort(nf,1); nf=nf[np.unique(s,axis=0,return_index=True)[1]] if len(nf) else nf
        if len(nf)>target: lo=h
        else: hi=h; best=(inv,nf,len(u))
    if best is None: return V,F
    inv,nf,nu=best
    cnt=np.bincount(inv,minlength=nu)[:,None]
    nv=np.stack([np.bincount(inv,weights=V[:,k],minlength=nu) for k in range(3)],1)/cnt
    used=np.unique(nf); remap=-np.ones(nu,int); remap[used]=np.arange(len(used))
    return nv[used],remap[nf]
meshes=[];allv=[]
TOT=330000; raw=sum(len(o['f']) for o in objs)
for o in objs:
    V=np.array([[float(x) for x in s.split()] for s in o['v']])
    F=np.array(o['f'])-1-o['v0']
    used=np.unique(F);r=-np.ones(len(V),int);r[used]=np.arange(len(used));V=V[used];F=r[F]
    t=max(120,int(len(F)/raw*TOT))
    V2,F2=dec(V,F,t); meshes.append((o['n'],V2,F2)); allv.append(V2)
A=np.vstack(allv);mn=A.min(0);mx=A.max(0);sc=(mx-mn).max()
print('tris',sum(len(m[2]) for m in meshes),'verts',len(A))
vb=bytearray();fb=bytearray();meta=[]
for n,V,F in meshes:
    q=np.round((V-mn)/sc*65535).astype(np.uint16)
    meta.append([n,len(V),len(F),len(vb)//2,len(fb)//2]); vb+=q.tobytes(); fb+=F.astype(np.uint16).tobytes()
nv=len(vb)//2
for m in meta: m[4]+=nv  # face offset relative to uint16 stream
blob=bytes(vb)+bytes(fb)
print('blob MB',len(blob)/1e6)
json.dump({'mn':mn.tolist(),'sc':float(sc),'meta':meta},open('meta.json','w'))
open('blob.b64','w').write(base64.b64encode(blob).decode())
