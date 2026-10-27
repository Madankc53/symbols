#!/usr/bin/env python3
"""Apply the shared header/footer/search, icons and AdSense tag to every page.
Idempotent: re-running replaces the marked blocks. Run after build_search_index.py."""
import re, json, glob, html, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
ADS = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1239173186536702" crossorigin="anonymous"></script>'
IDX = json.load(open('assets/search-index.json', encoding='utf8'))
SITE = 'https://symbols.thenepal.io'
T = {
 'en': dict(brand='The Nepal', sub='National Symbols Hub', bc_home='The Nepal', bc_hub='National Symbols', ph='Search symbols…', aria='Search national symbols of Nepal',
            hub='/', desc="Nepal's most complete reference for national symbols, culture, geography and heritage.",
            g=['Nature', 'Culture', 'Geography & Heritage', 'The Nepal Network'], about='About', contact='Contact', privacy='Privacy Policy',
            note='Educational content — verify with official Government of Nepal sources.', made='© 2026 The Nepal · symbols.thenepal.io · Made in Nepal', langname='Language', main='Main'),
 'ne': dict(brand='द नेपाल', sub='राष्ट्रिय चिन्ह केन्द्र', bc_home='द नेपाल', bc_hub='राष्ट्रिय चिन्हहरू', ph='चिन्ह खोज्नुहोस्…', aria='नेपालका राष्ट्रिय चिन्हहरू खोज्नुहोस्',
            hub='/ne/', desc='राष्ट्रिय चिन्ह, संस्कृति, भूगोल र सम्पदाबारे नेपालको सबैभन्दा पूर्ण सन्दर्भ सामग्री।',
            g=['प्रकृति', 'संस्कृति', 'भूगोल र सम्पदा', 'द नेपाल नेटवर्क'], about='हाम्रोबारे', contact='सम्पर्क', privacy='गोपनीयता नीति',
            note='शैक्षिक सामग्री — आधिकारिक नेपाल सरकारका स्रोतसँग पुष्टि गर्नुहोस्।', made='© 2026 द नेपाल · symbols.thenepal.io', langname='भाषा छान्नुहोस्', main='मुख्य'),
}
GROUP = {'nature': 0, 'culture': 1, 'geography': 2, 'heritage': 2}
NETWORK = [('TheNepal.io', 'https://thenepal.io/'), ('National Fruit Guide', 'https://nationalfruit.thenepal.io/'), ('National Dish Guide', 'https://nationalfood.thenepal.io/'), ('Madan KC', 'https://madankc.com.np')]
NETWORK_NE = [('द नेपाल', 'https://thenepal.io/'), ('राष्ट्रिय फल', 'https://nationalfruit.thenepal.io/'), ('राष्ट्रिय परिकार', 'https://nationalfood.thenepal.io/ne/'), ('मदन केसी', 'https://madankc.com.np')]
SVG_S = '<svg class="nx-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>'
SVG_B = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>'

def slug_of(url): return url.rstrip('/').split('/')[-1]
def label_for(lang, slug):
    for e in IDX[lang]:
        if slug_of(e['u']) == slug: return e['c'] or e['t']
    return None

def footer(lang):
    t = T[lang]; cols = [[], [], []]
    for e in IDX[lang]:
        if e.get('x'): continue
        cols[GROUP.get(e['g'], 2)].append('<li><a href="%s">%s</a></li>' % (e['u'], html.escape(e['c'] or e['t'])))
    net = ''.join('<li><a href="%s">%s</a></li>' % (u, html.escape(n)) for n, u in (NETWORK if lang == 'en' else NETWORK_NE))
    def col(i, items): return '<div><h2>%s</h2><ul>%s</ul></div>' % (t['g'][i], items)
    return ('<!--nx-footer-->\n<footer class="nx-footer" id="nx-footer"><div class="nx-fw"><div class="nx-fgrid">'
        '<div><a class="nx-fbrand" href="%s"><img src="/logo.png" width="40" height="40" alt="" loading="lazy"><b>%s</b></a><p>%s</p><p>symbols.thenepal.io</p></div>'
        '%s%s%s%s</div>'
        '<div class="nx-fbottom"><span>%s</span><nav aria-label="Site"><a href="https://thenepal.io/about/">%s</a><a href="https://thenepal.io/contact/">%s</a><a href="https://thenepal.io/privacy-policy/">%s</a></nav></div>'
        '<div class="nx-fbottom" style="border:0;margin-top:0;padding-top:10px"><span>%s</span></div>'
        '</div></footer>\n<!--/nx-footer-->') % (t['hub'], t['brand'], t['desc'], col(0, ''.join(cols[0])), col(1, ''.join(cols[1])), col(2, ''.join(cols[2])), col(3, net),
        t['made'], t['about'], t['contact'], t['privacy'], t['note'])

def header(lang, slug):
    t = T[lang]
    en_url = SITE + '/' + slug + '/'; ne_url = SITE + '/ne/' + slug + '/'
    lab = label_for(lang, slug) or slug
    if lang == 'en':
        sw = '<span aria-current="true">EN</span><a href="%s" hreflang="ne" lang="ne">नेपाली</a>' % ne_url
    else:
        sw = '<a href="%s" hreflang="en" lang="en">EN</a><span aria-current="true">नेपाली</span>' % en_url
    return ('<!--nx-header-->\n<div class="nx-header" id="nx-header">'
        '<nav class="nx-bc" aria-label="%s"><ol><li><a href="https://thenepal.io/">%s</a></li><li class="nx-sep" aria-hidden="true">/</li><li><a href="%s">%s</a></li><li class="nx-sep" aria-hidden="true">/</li><li aria-current="page">%s</li></ol></nav>'
        '<div class="nx-inner"><a class="nx-brand" href="%s" aria-label="%s — %s"><img src="/logo.png" width="42" height="42" alt=""><span><b>%s</b><small>%s</small></span></a>'
        '<div class="nx-right"><form class="nx-search" role="search" action="%s" method="get">%s<input type="search" name="q" placeholder="%s" aria-label="%s" autocomplete="off" enterkeyhint="search"><button type="submit" aria-label="%s">%s</button><div class="nx-suggest" hidden></div></form>'
        '<div class="nx-lang" role="group" aria-label="%s">%s</div></div></div></div>\n<!--/nx-header-->') % (
        'Breadcrumb' if lang == 'en' else 'ब्रेडक्रम्ब', t['bc_home'], SITE + t['hub'], t['bc_hub'], html.escape(lab),
        t['hub'], t['brand'], t['sub'], t['brand'], t['sub'], t['hub'], SVG_S, t['ph'], t['aria'], 'Search' if lang == 'en' else 'खोज्नुहोस्', SVG_B, t['langname'], sw)

def cut_balanced(s, start_pat, tag):
    """Remove an element whose opening tag matches start_pat (balanced on `tag`)."""
    m = re.search(start_pat, s)
    if not m: return s, False
    i = m.start(); depth = 0
    for t in re.finditer(r'<(/?)%s\b[^>]*>' % tag, s[i:]):
        depth += -1 if t.group(1) else 1
        if depth == 0:
            return s[:i] + s[i + t.end():], True
    raise SystemExit('unbalanced ' + start_pat)

def head_tags(is_hub, s):
    add = []
    if 'adsbygoogle' not in s: add.append(ADS)
    if 'rel="icon"' not in s: add.append('<link rel="icon" href="/logo.png" type="image/png">')
    if 'apple-touch-icon' not in s: add.append('<link rel="apple-touch-icon" href="/logo.png">')
    if 'rel="manifest"' not in s: add.append('<link rel="manifest" href="/manifest.json">')
    if 'name="theme-color"' not in s: add.append('<meta name="theme-color" content="#7E2A2A">')
    if '/assets/chrome.css' not in s: add.append('<link rel="stylesheet" href="/assets/chrome.css">')
    if not is_hub and '/assets/chrome.js' not in s: add.append('<script defer src="/assets/chrome.js"></script>')
    return add

def process(f):
    s = open(f, encoding='utf8').read()
    lang = 'ne' if f.startswith('ne/') else 'en'
    is_hub = f in ('index.html', 'ne/index.html')
    slug = None if is_hub else f.split('/')[-2]
    had = '<!--nx-header-->' in s
    # remove previous shared blocks
    s = re.sub(r'<!--nx-header-->.*?<!--/nx-header-->\n?', '', s, flags=re.S)
    s = re.sub(r'<!--nx-footer-->.*?<!--/nx-footer-->\n?', '', s, flags=re.S)
    # footer: replace old
    if '<footer' in s:
        s, _ = cut_balanced(s, r'<footer\b', 'footer')
    if not is_hub:
        s, a = cut_balanced(s, r'<div class="topbar">', 'div')
        s, b = cut_balanced(s, r'<header class="site">', 'header')
        if not (a or b or had): print('WARN no old header', f)
    # head
    add = head_tags(is_hub, s)
    if add: s = s.replace('</head>', '\n'.join(add) + '\n</head>', 1)
    if not is_hub:
        m = re.search(r'<body[^>]*>(\s*<a class="skip-link"[^>]*>[^<]*</a>)?', s)
        s = s[:m.end()] + '\n' + header(lang, slug) + s[m.end():]
    # footer goes before the first <script> that follows </main> or before </body>
    foot = footer(lang)
    m = re.search(r'</main>', s)
    if m and not is_hub:
        s = s[:m.end()] + '\n' + foot + s[m.end():]
    elif is_hub:
        m2 = re.search(r'<button id="top-btn"', s)
        s = s[:m2.start()] + foot + '\n\n' + s[m2.start():]
    else:
        s = s.replace('</body>', foot + '\n</body>', 1)
    if is_hub:
        s = s.replace('<div class="brand-logo" aria-hidden="true">न</div>', '<img src="/logo.png" width="42" height="42" alt="" style="border-radius:10px;display:block;flex:0 0 auto">')
    open(f, 'w', encoding='utf8').write(s)

files = [f for f in sorted(glob.glob('*/index.html') + glob.glob('ne/*/index.html') + ['index.html', 'ne/index.html']) if not f.startswith(('photos/', 'assets/', 'scripts/')) and f != 'ne/index.html/index.html']
for f in dict.fromkeys(files): process(f)
print(len(set(files)), 'pages processed')
