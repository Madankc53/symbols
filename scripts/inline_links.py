#!/usr/bin/env python3
"""Add first-occurrence contextual internal links in body <p> text (idempotent)."""
import re,sys,glob,os
B='https://symbols.thenepal.io/'
EN={'flag':[r'national flag',r'double-pennant flag'],'flower':[r'Lali Gurans',r'rhododendron'],
'everest':[r'Mount Everest',r'Sagarmatha'],'anthem':[r'national anthem',r'Sayaun Thunga Phulka'],
'color':[r'national colou?r',r'crimson red'],'emblem':[r'national emblem',r'coat of arms'],
'monument':[r'Dharahara'],'calendar':[r'Bikram Sambat'],'dress':[r'Daura Suruwal',r'Dhaka topi'],
'bird':[r'Himalayan Monal',r'Danphe'],'sport':[r'volleyball'],'currency':[r'Nepalese [Rr]upee'],
'cave':[r'Siddha Gufa'],'museum':[r'National Museum of Nepal'],'tree':[r'[Pp]eepal'],
'language':[r'Nepali language'],'butterfly':[r'Krishna Peacock'],'fish':[r'Golden Mahseer'],
'dance':[r'Deuda'],'animal':[r'national animal']}
NE={'flag':['राष्ट्रिय झण्डा'],'flower':['लालीगुराँस'],'everest':['सगरमाथा'],'anthem':['राष्ट्रिय गान'],
'color':['राष्ट्रिय रंग'],'emblem':['राष्ट्रिय प्रतीक','राजचिन्ह'],'monument':['धरहरा'],'calendar':['बिक्रम संवत्'],
'dress':['दौरा सुरुवाल','ढाका टोपी'],'bird':['डाँफे'],'sport':['भलिबल'],'currency':['नेपाली रुपैयाँ'],
'cave':['सिद्ध गुफा'],'museum':['राष्ट्रिय संग्रहालय'],'tree':['पीपल'],'butterfly':['कृष्ण मयुर'],'fish':['असला'],'dance':['देउडा'],'animal':['गाई']}
MAXN=5
def slug(f): return f.split('/')[-2].replace('national-','')
def proc(f,ne):
    pm=NE if ne else EN
    own=slug(f); s=open(f,encoding='utf-8').read().split('\n')
    pre=B+('ne/' if ne else '')
    done=set(); inb=False; n=0
    # targets already linked in body paragraphs
    for l in s:
        for m in re.finditer(r'href="'+re.escape(pre)+r'national-([a-z]+)/"',l):
            if re.match(r'\s*<p',l): done.add(m.group(1))
    out=[]
    for l in s:
        if '<details' in l: inb=True
        if inb or not re.match(r'\s*<p[ >].*</p>\s*$',l) or '<a ' in l or n>=MAXN:
            out.append(l)
            if '</details>' in l: inb=False
            continue
        parts=re.split(r'(<[^>]+>)',l)
        for t,pats in pm.items():
            if t==own or t in done or n>=MAXN: continue
            hit=False
            for i,p in enumerate(parts):
                if p.startswith('<') or hit: continue
                for pat in pats:
                    rx=re.compile(r'(?<![\wऀ-ॿ])'+(pat)) if ne else re.compile(r'\b'+pat+r'\b')
                    m=rx.search(p)
                    if m:
                        a=B+('ne/' if ne else '')+'national-'+('color' if t=='color' else t)+'/'
                        parts[i]=p[:m.start()]+'<a href="%s">%s</a>'%(a,m.group(0))+p[m.end():]
                        done.add(t); n+=1; hit=True; break
        out.append(''.join(parts))
    open(f,'w',encoding='utf-8').write('\n'.join(out))
    return n
tot=0
for f in sorted(glob.glob('national-*/index.html')):
    k=proc(f,False); tot+=k; print(f,k)
for f in sorted(glob.glob('ne/national-*/index.html')):
    k=proc(f,True); tot+=k; print(f,k)
print(tot)
