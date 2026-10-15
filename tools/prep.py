import numpy as np, json, re
names=[l.strip() for l in open('names.txt')]
objs=[];cur=None;vcount=0
with open('sk.obj','r') as f:
    for line in f:
        if line.startswith('o '):
            nm=line[2:].strip()
            if nm.startswith('Rectus_abdominis_muscle.er'): break
            cur={'n':nm,'v':[],'f':[],'v0':vcount};objs.append(cur)
        elif line.startswith('v '):
            vcount+=1
            if cur is not None: cur['v'].append(line[2:])
        elif line.startswith('f ') and cur is not None:
            idx=[int(t.split('/')[0]) for t in line[2:].split()]
            for k in range(1,len(idx)-1): cur['f'].append((idx[0],idx[k],idx[k+1]))
objs=[o for o in objs if not o['n'].startswith('Cross_Section') and o['v'] and o['f']]
print(len(objs),sum(len(o['f']) for o in objs))
import pickle;pickle.dump(objs,open('bones.pkl','wb'))
