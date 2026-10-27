#!/usr/bin/env python3
"""Build assets/search-index.json from the symbol cards on the two hub pages."""
import re, json, html, sys
def cards(path, lang):
    s = open(path, encoding='utf8').read()
    out = []
    for m in re.finditer(r'<a href="([^"]+)" class="sym-card ([^"]*)"([^>]*)>(.*?)</a>', s, re.S):
        href, cls, attrs, body = m.groups()
        a = dict(re.findall(r'data-([a-z-]+)="([^"]*)"', attrs))
        h3 = re.search(r'<h3>(.*?)</h3>', body, re.S)
        if 'soon' in cls or not h3: continue
        u = href if href.startswith('http') else 'https://symbols.thenepal.io' + href
        ext = 'symbols.thenepal.io' not in u
        out.append({
            't': html.unescape(re.sub(r'<[^>]+>', '', h3.group(1))).strip(),
            'n': html.unescape(a.get('nepali', '')),
            'k': html.unescape(a.get('keywords', '')) + ' ' + html.unescape(a.get('scientific', '')),
            'c': html.unescape(a.get('category-label', '')),
            'g': a.get('cat', ''),
            'u': u if not ext else u,
            **({'x': 1} if ext else {}),
        })
    return out
idx = {'en': cards('index.html', 'en'), 'ne': cards('ne/index.html', 'ne')}
json.dump(idx, open('assets/search-index.json', 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
print({k: len(v) for k, v in idx.items()})
