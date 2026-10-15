import re,collections
names=[l.strip() for l in open('names.txt')]
EXC=re.compile(r'ligament|capsule|disc|nucleus|annulus|joint|bursa|fascia|membrane|cartilage|tend|aponeurosis|retinaculum|sheath|septum|raphe|region|node|arter|vein|nerve|plexus|duct|gland|ventric|atri|valve|papillary|heart|vessel|trunk|space|canal|fossa|sinus|vertebra|bone|menisc|labrum|synov|pulley|cruciate|triangular|plate|fat|skin|cavity|foramen|hiatus|ring|arch|sulcus|lobe|cortex|tract|nerve|frenul|linea|cord|symphysis|tarsus|vena|insertion|zona',re.I)
def split(n):
    m=re.search(r'\.([a-z0-9]+)$',n); s=m[1] if m else ''
    b=n[:m.start()] if m else n
    side=s[-1] if s and s[-1] in 'rl' else ''
    t='e' if s.startswith('e') else 'o' if s.startswith('o') else 'p'
    return b,s,side,t
mend=next(i for i,n in enumerate(names) if i>1400 and re.search(r'arter|vein|ventric|atrium|valve',n,re.I))
def select():
    mus=[];ner=[]
    for i,n in enumerate(names):
        b,s,side,t=split(n)
        if 280<=i<mend and not EXC.search(b): mus.append((i,b,s,side,t))
        elif re.search(r'nerve|plexus|Spinal_cord|ganglion',b,re.I) and not re.search(r'venous|choroid|arter|vein|nucleus|vessel|root|node|lymph|tract|region|sulcus|canal|ridge|fossa|foramen|groove',b,re.I): ner.append((i,b,s,side,t))
    # muscle dedupe
    g=collections.defaultdict(list)
    for x in mus: g[(x[1],x[3])].append(x)
    keep=[]
    for k,v in g.items():
        for want in 'epo':
            w=[x for x in v if x[4]==want]
            if w: keep+=w;break
    bases={x[1].lower().replace('_muscle','') for x in keep if x[4]!='o' or True}
    out=[]
    for x in keep:
        par=re.sub(r'^.*?_(heads?|parts?|belly|bellies)_of_','',x[1]).lower().replace('_muscle','')
        if par!=x[1].lower().replace('_muscle','') and par in bases and not par.startswith('('): continue
        out.append(x)
    return out,ner
if __name__=='__main__':
    m,n=select();print(mend,len(m),len(n))
    import random;random.seed(1)
    print([x[1] for x in random.sample(m,45) if 'muscle' not in x[1].lower()])
    print(sorted({x[1] for x in m if 'uscle' not in x[1]})[:90])
