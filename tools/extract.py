import numpy as np, pickle, cls
m,n=cls.select()
want={x[0]:('otot',x) for x in m}; want.update({x[0]:('saraf',x) for x in n})
out={'otot':[],'saraf':[]}
idx=-1;vc=0;cur=None
def fin():
    global cur
    if cur and cur['v'] and cur['f']:
        V=np.fromstring(''.join(cur['v']),sep=' ').reshape(-1,3).astype(np.float32)
        F=[];
        for s in cur['f']:
            t=[int(a.split('/')[0]) for a in s.split()]
            for k in range(1,len(t)-1): F.append((t[0],t[k],t[k+1]))
        F=np.array(F,dtype=np.int64)-1-cur['v0']
        out[cur['layer']].append((cur['x'],V,F))
    cur=None
with open('sk.obj','r') as f:
    for line in f:
        c=line[0]
        if c=='o' and line[1]==' ':
            fin(); idx+=1
            if idx in want: cur={'layer':want[idx][0],'x':want[idx][1],'v':[],'f':[],'v0':vc}
        elif c=='v' and line[1]==' ':
            vc+=1
            if cur is not None: cur['v'].append(line[2:])
        elif c=='f' and cur is not None: cur['f'].append(line[2:])
fin()
for k,v in out.items(): print(k,len(v),sum(len(a[2]) for a in v))
pickle.dump(out,open('ms.pkl','wb'),protocol=4)
print('done')
