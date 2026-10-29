#!/usr/bin/env python3
"""Idempotent technical-SEO head hygiene for every page:
 - robots meta with max-image-preview:large (needed for large Discover/Search image previews)
 - og:site_name, og:image:width/height/alt, theme-color
 - visible 'last reviewed' line (from Article.dateModified) just above the shared footer
Run after scripts/sync_jsonld.py --touch."""
import re, os, glob, sys, html, datetime
from PIL import Image
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
files = ['index.html', 'ne/index.html'] + sorted(glob.glob('*/index.html') + glob.glob('ne/*/index.html'))
files = [f for f in dict.fromkeys(files) if not f.startswith(('photos/', 'assets/', 'scripts/'))]
ROBOTS = '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">'
NE_DIGITS = str.maketrans('0123456789', '०१२३४५६७८९')
MONTHS = ['January','February','March','April','May','June','July','August','September','October','November','December']
for f in files:
    s = open(f, encoding='utf8').read(); o = s
    ne = f.startswith('ne/')
    if '<meta name="robots"' not in s:
        s = re.sub(r'(<meta name="viewport"[^>]*>)', r'\1\n' + ROBOTS, s, count=1)
    if 'name="theme-color"' not in s:
        s = re.sub(r'(<meta name="viewport"[^>]*>)', r'\1\n<meta name="theme-color" content="#7E2A2A">', s, count=1)
    if 'og:site_name' not in s:
        name = 'नेपालका राष्ट्रिय चिन्हहरू' if ne else 'National Symbols of Nepal'
        s = re.sub(r'(<meta property="og:url"[^>]*>)', r'\1\n<meta property="og:site_name" content="%s">' % name, s, count=1)
    m = re.search(r'<meta property="og:image" content="https://symbols\.thenepal\.io(/[^"]+)">', s)
    if m and os.path.exists('.' + m.group(1)):
        extra = ''
        if 'og:image:width' not in s:
            w, h = Image.open('.' + m.group(1)).size
            extra += '\n<meta property="og:image:width" content="%d">\n<meta property="og:image:height" content="%d">' % (w, h)
        if 'og:image:alt' not in s:
            fn = os.path.basename(m.group(1))
            am = re.search(r'<img[^>]*src="[^"]*%s"[^>]*alt="([^"]+)"' % re.escape(fn), s) or re.search(r'<img[^>]*alt="([^"]+)"[^>]*src="[^"]*%s"' % re.escape(fn), s)
            alt = am.group(1) if am else html.unescape(re.sub(r'<[^>]+>', '', (re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S) or [None, ''])[1])).strip()
            if alt: extra += '\n<meta property="og:image:alt" content="%s">' % alt.replace('"', '&quot;')
        if extra: s = s.replace(m.group(0), m.group(0) + extra, 1)
    d = re.search(r'"dateModified":\s*"(\d{4})-(\d{2})-(\d{2})"', s)
    if d and '<!--nx-footer-->' in s:
        y, mo, da = d.groups()
        txt = ('पछिल्लो समीक्षा: ' + ('%s-%s-%s' % (y, mo, da)).translate(NE_DIGITS)) if ne else 'Last reviewed: %d %s %s' % (int(da), MONTHS[int(mo) - 1], y)
        blk = '<!--nx-updated--><p class="nx-updated"><time datetime="%s-%s-%s">%s</time></p><!--/nx-updated-->' % (y, mo, da, txt)
        if '<!--nx-updated-->' in s:
            s = re.sub(r'<!--nx-updated-->.*?<!--/nx-updated-->', blk, s, flags=re.S)
        else:
            s = s.replace('<!--nx-footer-->', blk + '\n<!--nx-footer-->', 1)
    if s != o:
        open(f, 'w', encoding='utf8').write(s); print('updated', f)
