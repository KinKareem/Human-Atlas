import numpy as np, pickle, json, base64, cls
src=open('dec2.py').read().split("T={")[0]
exec(src)   # defines dec(), loads ms.pkl as 'out'
org=pickle.load(open('org.pkl','rb'))
items=[(cls.names[i],V,F) for i,V,F in org]
for x,V,F in out['otot']:
    if x[1]=='Diaphragm': items.append((cls.names[x[0]],V,F))
raw=sum(len(a[2]) for a in items); ms=[]
for n,V,F in items:
    used=np.unique(F); r=-np.ones(len(V),int); r[used]=np.arange(len(used)); V=V[used].astype(np.float64); F=r[F]
    t=max(120,int(len(F)/raw*170000)); V2,F2=dec(V,F,t); ms.append((n,V2,F2))
A=np.vstack([m[1] for m in ms]); mn=A.min(0); sc=float((A.max(0)-mn).max())
vb=bytearray(); fb=bytearray(); meta=[]
for n,V,F in ms:
    q=np.round((V-mn)/sc*65535).astype(np.uint16)
    meta.append([n,len(V),len(F),len(vb)//2,len(fb)//2]); vb+=q.tobytes(); fb+=F.astype(np.uint16).tobytes()
nv=len(vb)//2
for m in meta: m[4]+=nv
blob=bytes(vb)+bytes(fb)
print(len(ms),'tris',sum(m[2] for m in meta),'MB',len(blob)/1e6)
json.dump({'mn':mn.tolist(),'sc':sc,'meta':meta},open('meta_organ.json','w'))
open('blob_organ.b64','w').write(base64.b64encode(blob).decode())
print([m[0] for m in meta if 'Diaphragm' in m[0]])
