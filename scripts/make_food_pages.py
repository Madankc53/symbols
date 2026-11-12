#!/usr/bin/env python3
"""Generate national-fruit and national-food pages (EN + NE).
CSS is reused verbatim from the national-fish pages; chrome (header/footer/updated line) is added by
apply_chrome.py / seo_meta.py afterwards. Run from repo root: python3 scripts/make_food_pages.py"""
import re, json, html, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
SITE = 'https://symbols.thenepal.io'
DATE = '2026-11-10'

EXTRA_CSS = '''
/* fruit & food additions */
.tl{list-style:none;border-left:3px solid var(--marigold);margin:14px 0 6px 6px;padding-left:18px;}
.tl li{position:relative;margin-bottom:14px;}
.tl li::before{content:"";position:absolute;left:-26px;top:6px;width:11px;height:11px;border-radius:50%;background:var(--marigold-deep);border:2px solid var(--cream);}
.tl b{display:block;color:var(--maroon-dark);font-size:.9rem;}
.thali{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px;margin:14px 0;}
.thali div{background:var(--white);border:1px solid var(--rule);border-radius:var(--radius);padding:14px 14px 12px;}
.thali .ic{font-size:1.5rem;display:block;margin-bottom:4px;}
.thali b{display:block;color:var(--maroon-dark);}
.thali small{display:block;color:var(--ink-soft);font-size:.8rem;margin-top:2px;}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0;}
.chips span{background:var(--paper);border:1px solid var(--rule);border-radius:999px;padding:6px 14px;font-size:.86rem;font-weight:600;color:var(--maroon-dark);}
.status{border:1px solid var(--rule);border-left:5px solid var(--forest);background:var(--white);border-radius:var(--radius);padding:14px 16px;margin:14px 0;}
.status.warn{border-left-color:var(--marigold-deep);}
.status b{color:var(--maroon-dark);}
'''

def base_css(lang):
    p = ('ne/' if lang == 'ne' else '') + 'national-fish/index.html'
    return re.search(r'<style>(.*?)</style>', open(p, encoding='utf-8').read(), re.S).group(1) + EXTRA_CSS

L = {
 'en': dict(facts='Quick Facts', nepali='Nepali', latin='Latin script', say='Pronunciation', dyk='✦ Did you know?', faq='Frequently Asked Questions',
            more='Explore more national symbols', cta='Explore all 22 National Symbols →', hubname='National Symbols', home='The Nepal',
            hub_t='National Symbols of Nepal', other_lang='ne', source='Source', sources='Sources'),
 'ne': dict(facts='छोटो तथ्यहरू', nepali='नेपाली', latin='रोमन लिपि', say='उच्चारण', dyk='✦ के तपाईंलाई थाहा छ?', faq='बारम्बार सोधिने प्रश्नहरू',
            more='अन्य राष्ट्रिय चिन्हहरू हेर्नुहोस्', cta='सबै २२ राष्ट्रिय चिन्हहरू हेर्नुहोस् →', hubname='राष्ट्रिय चिन्ह', home='द नेपाल',
            hub_t='नेपालका राष्ट्रिय चिन्हहरू', other_lang='en', source='स्रोत', sources='स्रोतहरू'),
}

def esc(x): return html.escape(x, quote=True)
def strip(x): return html.unescape(re.sub(r'<[^>]+>', '', x)).strip()

def build(pg, lang):
    t = L[lang]; d = pg[lang]
    slug = pg['slug']; path = ('/ne' if lang == 'ne' else '') + '/' + slug + '/'
    url = SITE + path; alt_url = SITE + ('/' if lang == 'ne' else '/ne/') + slug + '/'
    en_url = SITE + '/' + slug + '/'; ne_url = SITE + '/ne/' + slug + '/'
    img = SITE + '/photos/' + pg['photo']
    faq_ld = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in d['faq']]
    ld = [
     {"@context": "https://schema.org", "@type": "Article", "inLanguage": lang, "dateModified": DATE, "headline": d['og_title'], "description": d['ld_desc'],
      "image": img, "author": {"@type": "Organization", "name": "The Nepal"}, "publisher": {"@type": "Organization", "name": "The Nepal", "url": "https://thenepal.io"},
      "mainEntityOfPage": url, "about": {"@type": "Thing", "name": pg['about_name'], "sameAs": pg['about_sameas']},
      "mentions": [{"@type": "Thing", "name": "Nepal", "sameAs": "https://en.wikipedia.org/wiki/Nepal"}, {"@type": "Thing", "name": "National symbols of Nepal", "sameAs": "https://en.wikipedia.org/wiki/National_symbols_of_Nepal"}]},
     {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": t['home'], "item": "https://thenepal.io"},
        {"@type": "ListItem", "position": 2, "name": t['hubname'], "item": SITE + ('/ne/' if lang == 'ne' else '/')},
        {"@type": "ListItem", "position": 3, "name": d['crumb'], "item": url}]},
     {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_ld},
     {"@context": "https://schema.org", "@type": "ImageObject", "contentUrl": img, "width": 1600, "height": 900, "caption": d['img_caption'], "representativeOfPage": True},
     {"@context": "https://schema.org", "@type": "Organization", "name": "The Nepal", "url": "https://thenepal.io", "logo": SITE + "/logo.png", "sameAs": [SITE + "/"]},
     {"@context": "https://schema.org", "@type": "WebSite", "name": "National Symbols of Nepal", "url": SITE + "/"},
     {"@context": "https://schema.org", "@type": "WebPage", "name": d['og_title'], "url": url, "isPartOf": {"@type": "WebSite", "name": "National Symbols of Nepal", "url": SITE + "/"}, "inLanguage": lang,
      "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".hero-desc", ".facts"]}},
     *([] if pg.get('noitemlist') else [{"@context": "https://schema.org", "@type": "ItemList", "name": "National Symbols of Nepal", "url": SITE + "/", "description": d['itemlist_desc'], "numberOfItems": 22}]),
    ]
    ldh = '\n'.join('<script type="application/ld+json">\n%s\n</script>' % json.dumps(x, ensure_ascii=False, indent=2) for x in ld)
    facts = ''.join('<div class="fact"><dt>%s</dt><dd%s>%s</dd></div>' % (k, ' lang="ne"' if (lang == 'en' and k0) else '', v) for (k, v, k0) in d['facts'])
    tags = ''.join('<span class="tag">%s</span>' % x for x in d['tags'])
    faq = ''.join('<details class="faq-item"><summary>%s</summary><p>%s</p></details>' % (q, a) for q, a in d['faq'])
    rel = ''.join('<a href="%s">%s</a>' % (u, x) for u, x in d['related'])
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
<title>{esc(d['title'])}</title>
<meta name="description" content="{esc(d['desc'])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="ne" href="{ne_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">

<meta property="og:type" content="article">
<meta property="og:title" content="{esc(d['og_title'])}">
<meta property="og:description" content="{esc(d['og_desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="National Symbols of Nepal">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="1600">
<meta property="og:image:height" content="900">
<meta property="og:image:alt" content="{esc(d['img_alt'])}">
<meta name="twitter:card" content="summary_large_image">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=Noto+Sans+Devanagari:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="preload" as="image" fetchpriority="high" href="{img}">

{ldh}
<style>{base_css(lang)}</style>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1239173186536702" crossorigin="anonymous"></script>
<link rel="icon" href="/logo.png" type="image/png">
<link rel="apple-touch-icon" href="/logo.png">
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#7E2A2A">
<link rel="stylesheet" href="/assets/chrome.css">
<script defer src="/assets/chrome.js"></script>
</head>
<body>

<div class="garland" aria-hidden="true"></div>

<header class="hero">
  <div class="wrap">
    <span class="eyebrow">{d['eyebrow']}</span>
    <h1>{d['h1']}</h1>
    <p class="hero-desc">{d['hero']}</p>
    <div class="hero-tags">{tags}</div>
    <figure class="hero-photo">
      <img src="{img}" alt="{esc(d['img_alt'])}" width="880" height="340" fetchpriority="high" decoding="async">
    </figure>
    <p class="caption">{d['caption']}</p>
  </div>
</header>

<main class="wrap">

  <div class="facts">
    <h2>{t['facts']}</h2>
    <dl class="facts-grid">{facts}</dl>
  </div>

  <div class="pronounce">
    <div><div class="p-label">{t['nepali']}</div><div class="p-value nepali">{d['pron'][0]}</div></div>
    <div><div class="p-label">{t['latin']}</div><div class="p-value">{d['pron'][1]}</div></div>
    <div><div class="p-label">{t['say']}</div><div class="p-value say">{d['pron'][2]}</div></div>
  </div>

  <article>
{d['body']}
    <section id="faq">
      <h2>{t['faq']}</h2>
      {faq}
    </section>
  </article>

  <div class="related">
    <h2>{t['more']}</h2>
    <p>{d['related_p']}</p>
    <div class="related-links">{rel}</div>
  </div>

  <div class="final-cta">
    <a href="{SITE + ('/ne/' if lang == 'ne' else '/')}">{t['cta']}</a>
  </div>
</main>
<!--nx-footer-->
<!--/nx-footer-->
</body>
</html>
'''

exec(open(os.path.join(ROOT, 'scripts', 'food_content.py'), encoding='utf-8').read())
_ny = os.path.join(ROOT, 'scripts', 'newyear_content.py')
if os.path.exists(_ny):
    exec(open(_ny, encoding='utf-8').read()); PAGES = PAGES + EXTRA_PAGES

for pg in PAGES:
    for lang in ('en', 'ne'):
        out = ('ne/' if lang == 'ne' else '') + pg['slug'] + '/index.html'
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, 'w', encoding='utf-8').write(build(pg, lang))
        print(out)
