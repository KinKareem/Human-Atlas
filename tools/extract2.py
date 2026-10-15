import numpy as np, pickle, cls, re
CART={'Lateral_process_of_nasal_septal_cartilage','Nasal_septal_cartilage','Thyroid_cartilage','Cricoid_cartilage','Arytenoid_cartilage','Corniculate_cartilage','Major_alar_cartilage'}
want=set(range(4460,4517))|set(range(4560,4566))|{4567,4568,4569,4570,4571}
want|={i for i,n in enumerate(cls.names[:70]) if cls.split(n)[0] in CART}
print(len(want),flush=True)
out=[];idx=-1;vc=0;cur=None
def fin():
    global cur
    if cur and cur['v'] and cur['f']:
        V=np.fromstring(''.join(cur['v']),sep=' ').reshape(-1,3).astype(np.float32)
        F=[]
        for s in cur['f']:
            t=[int(a.split('/')[0]) for a in s.split()]
            for k in range(1,len(t)-1): F.append((t[0],t[k],t[k+1]))
        out.append((cur['i'],V,np.array(F,dtype=np.int64)-1-cur['v0']))
    cur=None
with open('sk.obj','r') as f:
    for line in f:
        c=line[0]
        if c=='o' and line[1]==' ':
            fin(); idx+=1
            if idx in want: cur={'i':idx,'v':[],'f':[],'v0':vc}
            if idx>4571: break
        elif c=='v' and line[1]==' ':
            vc+=1
            if cur is not None: cur['v'].append(line[2:])
        elif c=='f' and cur is not None: cur['f'].append(line[2:])
fin()
print(len(out),sum(len(a[2]) for a in out))
pickle.dump(out,open('org.pkl','wb'),protocol=4);print('done')
