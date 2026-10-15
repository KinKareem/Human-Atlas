import numpy as np, cls
want=set(map(int,open('vs_want.txt').read().split(',')))
mx=max(want); idx=-1; vc=0; cur=None; n=0
def fin():
    global cur,n
    if cur and cur['v'] and cur['f']:
        V=np.fromstring(''.join(cur['v']),sep=' ').reshape(-1,3).astype(np.float32)
        F=[]
        for s in cur['f']:
            t=[int(a.split('/')[0]) for a in s.split()]
            for k in range(1,len(t)-1): F.append((t[0],t[k],t[k+1]))
        F=np.array(F,dtype=np.int64)-1-cur['v0']
        np.savez(f'vs/{cur["i"]}.npz',V=V,F=F.astype(np.int32)); n+=1
    cur=None
with open('sk.obj','r') as f:
    for line in f:
        c=line[0]
        if c=='o' and line[1]==' ':
            fin(); idx+=1
            if idx>mx: break
            if idx in want: cur={'i':idx,'v':[],'f':[],'v0':vc}
        elif c=='v' and line[1]==' ':
            vc+=1
            if cur is not None: cur['v'].append(line[2:])
        elif c=='f' and cur is not None: cur['f'].append(line[2:])
fin(); print('saved',n,flush=True)
