import numpy as np, pickle, cls, re

want={4520,4521}|set(range(4528,4546))
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
            if idx>4545: break
        elif c=='v' and line[1]==' ':
            vc+=1
            if cur is not None: cur['v'].append(line[2:])
        elif c=='f' and cur is not None: cur['f'].append(line[2:])
fin()
print(len(out),sum(len(a[2]) for a in out))
pickle.dump(out,open('rep.pkl','wb'),protocol=4);print('done')
