#!/usr/bin/env python3
"""Rebuilds the homepage 'New and updated' block (EN + NE) from data/latest.json.
To publish a new or refreshed page on the homepage: add or edit its entry in data/latest.json (set "date" to today, YYYY-MM-DD),
then run: python3 scripts/update_latest.py. The newest 5 entries by date are shown; the block's 'last updated' date is the newest date."""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MONTHS = {'en': ['January','February','March','April','May','June','July','August','September','October','November','December'],
          'ne': ['जनवरी','फेब्रुअरी','मार्च','अप्रिल','मे','जुन','जुलाई','अगस्ट','सेप्टेम्बर','अक्टोबर','नोभेम्बर','डिसेम्बर']}
def dev(n): return str(n).translate(str.maketrans('0123456789', '०१२३४५६७८९'))
def block(lang, items):
    pre = '' if lang == 'en' else '/ne'
    top = sorted(items, key=lambda e: e['date'], reverse=True)[:5]
    y, m, d = top[0]['date'].split('-'); m = int(m); d = int(d)
    style = 'color:var(--maroon-dark);font-weight:600;text-decoration:underline;text-underline-offset:3px'
    lis = ''.join('<li style="margin:6px 0"><a style="%s" href="%s/%s/">%s</a></li>' % (style, pre, e['slug'], e[lang]) for e in top)
    if lang == 'en':
        h, sub = 'New and updated', 'Latest counts and dates, last updated %d %s %s.' % (d, MONTHS['en'][m-1], y)
    else:
        h, sub = 'नयाँ र अद्यावधिक', 'पछिल्ला गणना र मितिहरू, अन्तिम अद्यावधिक %s %s %s।' % (dev(d), MONTHS['ne'][m-1], dev(y))
    return ('<!-- LATEST:START -->\n<div class="wrap">\n  <div class="explore-more" id="latest">\n    <h3>%s</h3>\n    <p>%s</p>\n'
            '    <ul style="list-style:none;padding:0;margin:0;font-size:1rem">%s</ul>\n  </div>\n</div>\n<!-- LATEST:END -->') % (h, sub, lis)
def main():
    items = json.load(open(os.path.join(ROOT, 'data', 'latest.json'), encoding='utf-8'))
    for e in items:
        for l, pre in (('en', ''), ('ne', 'ne/')):
            if not os.path.exists(os.path.join(ROOT, pre + e['slug'], 'index.html')): sys.exit('missing page: %s%s' % (pre, e['slug']))
    for f, lang in (('index.html', 'en'), ('ne/index.html', 'ne')):
        p = os.path.join(ROOT, f); t = open(p, encoding='utf-8').read()
        new = block(lang, items)
        if '<!-- LATEST:START -->' in t:
            t = re.sub(r'<!-- LATEST:START -->.*?<!-- LATEST:END -->', lambda m: new, t, count=1, flags=re.S)
        else:
            t = re.sub(r'<!-- NEW AND UPDATED -->\n<div class="wrap">.*?</div>\n</div>\n', lambda m: new + '\n', t, count=1, flags=re.S)
        open(p, 'w', encoding='utf-8').write(t); print('updated', f)
if __name__ == '__main__': main()
