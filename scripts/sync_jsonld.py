#!/usr/bin/env python3
"""Mechanical structured-data hygiene for every symbol page:
 - FAQPage JSON-LD is rebuilt from the visible <details> FAQ (only if every JSON question is visible)
 - WebSite.potentialAction (SearchAction) removed (hub search has no URL parameter... it takes ?q= only
   on the hub, which Google no longer uses for sitelinks search)
 - ImageObject gets the real pixel size of the photo
 - Article gets inLanguage; dateModified set when --touch is given"""
import re, json, html, glob, os, sys
from PIL import Image
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
touch = '--touch' in sys.argv
files = [a for a in sys.argv[1:] if not a.startswith('--')] or sorted(glob.glob('*/index.html') + glob.glob('ne/*/index.html'))
for f in files:
    if f.startswith(('photos/', 'assets/', 'scripts/')): continue
    s = open(f, encoding='utf8').read(); o = s
    lang = 'ne' if f.startswith('ne/') else 'en'
    det = re.findall(r'<details[^>]*>\s*<summary[^>]*>(.*?)</summary>\s*(.*?)</details>', s, re.S)
    vis = []
    for q, a in det:
        q = html.unescape(re.sub(r'<[^>]+>', '', q)).strip()
        if '▾' in q or '📑' in q: continue
        vis.append((q, html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', a))).strip()))
    def faq(m):
        d = json.loads(m.group(2))
        if d.get('@type') != 'FAQPage': return m.group(0)
        names = {q['name'] for q in d['mainEntity']}
        if not vis or not names <= {q for q, _ in vis}:
            print('SKIP faq', f); return m.group(0)
        ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in vis]}
        return m.group(1) + json.dumps(ld, ensure_ascii=False, indent=2) + m.group(3)
    s = re.sub(r'(<script type="application/ld\+json">\s*)(\{.*?\})(\s*</script>)', faq, s, flags=re.S)
    s = re.sub(r',\s*"potentialAction":\s*\{[^{}]*"SearchAction"[^{}]*\}', '', s, flags=re.S)
    def img(m):
        blk = m.group(0)
        mm = re.search(r'"contentUrl":\s*"https://symbols\.thenepal\.io(/[^"]+)"', blk)
        if not mm or not os.path.exists('.' + mm.group(1)): return blk
        w, h = Image.open('.' + mm.group(1)).size
        blk = re.sub(r'\s*"(width|height)":\s*\d+,?', '', blk)
        return re.sub(r'("contentUrl":\s*"[^"]+",)', lambda k: k.group(1) + '\n  "width": %d,\n  "height": %d,' % (w, h), blk, count=1)
    s = re.sub(r'\{[^{}]*"@type":\s*"ImageObject"[^{}]*\}', img, s)
    def art(m):
        blk = m.group(0)
        if '"inLanguage"' not in blk: blk = re.sub(r'("@type":\s*"Article",)', r'\1\n  "inLanguage": "%s",' % lang, blk, count=1)
        if touch: blk = re.sub(r'("dateModified":\s*")[^"]+', r'\g<1>2026-10-28', blk)
        return blk
    s = re.sub(r'<script type="application/ld\+json">\s*\{[^<]*?"@type":\s*"Article".*?</script>', art, s, flags=re.S)
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S): json.loads(m.group(1))
    if s != o:
        open(f, 'w', encoding='utf8').write(s); print('updated', f)
